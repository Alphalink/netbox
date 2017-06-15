from collections import OrderedDict

from mptt.models import MPTTModel, TreeForeignKey

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Count, Q, ObjectDoesNotExist
from django.utils.encoding import python_2_unicode_compatible

from dcim.models import Device, InventoryItem, DeviceType
from circuits.models import Circuit
from extras.models import CustomFieldModel, CustomField, CustomFieldValue
from extras.rpc import RPC_CLIENTS
from tenancy.models import Tenant
from utilities.fields import ColorField, NullableCharField
from utilities.managers import NaturalOrderByManager
from utilities.models import CreatedUpdatedModel
from utilities.utils import csv_format

from .fields import ASNField, MACAddressField


#
# Cluster
#

class ClusterManager(NaturalOrderByManager):

    def get_queryset(self):
        return self.natural_order_by('name')


@python_2_unicode_compatible
class Cluster(CreatedUpdatedModel):
    """
    A cluster is a group of hypervisors whose support virtual resources
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    comments = models.TextField(blank=True)
    cpu = models.PositiveSmallIntegerField(default=12, verbose_name='CPU Number',
                                           help_text='Number of CPU in cluster')
    memory = models.PositiveIntegerField(default=8192, verbose_name='Memory (MB)',
                                           help_text='Total memory (in MB) in cluster')

    objects = ClusterManager()

    class Meta:
      ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('alphalink:cluster', args=[self.slug])

    def resource_used(self, type):
        """
        Determine the utilization of type (CPU|RAM) of the cluster and return it
        """
        resource_device_type = DeviceType.objects.filter(model="VM Qemu/KVM")
        resources = Device.objects.filter(cluster__name=self.name, device_type=resource_device_type)
        type_used = 0
        for resource in resources:
          resource_modules = InventoryItem.objects.filter(device=resource, name=type)
          for module in resource_modules:
            type_used = type_used + int(module.part_id)
        return type_used

    def cpu_utilization(self):
        """
        Get the utilization cpu of the cluster and return it as a percentage.
        """
        cpu_used = self.resource_used("CPU")
        return int(float(cpu_used) / self.cpu * 100)

    def ram_utilization(self):
        """
        Determine the utilization memory of the cluster and return it as a percentage.
        """
        ram_used = self.resource_used("RAM")
        return int(float(ram_used) / self.memory * 100)
