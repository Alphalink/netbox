from copy import deepcopy
import re
from natsort import natsorted
from operator import attrgetter

from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.db.models import Count,Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import urlencode
from django.views.generic import View

from ipam.models import Prefix, IPAddress, Service, VLAN
from dcim.models import Device, DeviceType, InventoryItem
from dcim.forms import DeviceForm
from circuits.models import Circuit
from extras.models import Graph, TopologyMap, GRAPH_TYPE_INTERFACE, GRAPH_TYPE_SITE
from utilities.forms import ConfirmationForm
from utilities.views import (
    BulkDeleteView, BulkEditView, BulkImportView, ObjectDeleteView, ObjectEditView, ObjectListView,
)

from . import filters, forms, tables
from .models import (
    Cluster,
)

class Resource():
    id = 0
    name = ""
    cpu = 0
    memory = 0


#
# Cluster
#

class ClusterListView(ObjectListView):
    queryset = Cluster.objects.all()
    table = tables.ClusterTable
    template_name = 'alphalink/cluster_list.html'


def cluster(request, slug):

    resource_device_type = get_object_or_404(DeviceType.objects.filter(model="VM Qemu/KVM"))

    cluster = get_object_or_404(Cluster.objects.all(), slug=slug)
    hypervisors = Device.objects.filter(cluster=cluster).exclude(device_type=resource_device_type)
    resources = Device.objects.filter(cluster=cluster, device_type=resource_device_type)

    total_used = { 'RAM': 0, 'CPU': 0}
    # Get CPU and memory for each resource
    resource_modules = []
    for resource in resources:
      tmp_module = Resource()
      tmp_module.id = resource.id
      tmp_module.name = resource.name
      tmp_module.memory = 0
      tmp_module.cpu = 0
      modules_resource = InventoryItem.objects.filter(device=resource).filter(Q(name="CPU") | Q(name="RAM"))
      for module in modules_resource:
	if module.name == "CPU":
          tmp_module.cpu = tmp_module.cpu + int(module.part_id)
	else:
          tmp_module.memory = tmp_module.memory + int(module.part_id)
        total_used[module.name] = total_used[module.name] + int(module.part_id)
      resource_modules.append(tmp_module)

    print(resource_modules)

    return render(request, 'alphalink/cluster.html', {
        'cluster': cluster,
        'hypervisors': hypervisors,
        'total_cpu_free': cluster.cpu - total_used['CPU'],
        'total_ram_free': cluster.memory - total_used['RAM'],
        'resources': resources,
        'resource_module': resource_modules,
    })


class ClusterEditView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'alphalink.change_cluster'
    model = Cluster
    form_class = forms.ClusterForm
    template_name = 'alphalink/cluster_edit.html'
    default_return_url = 'alphalink:cluster_list'

class ClusterBulkEditView(PermissionRequiredMixin, BulkEditView):
    permission_required = 'alphalink.change_cluster'
    cls = Cluster
    #filter = filters.SiteFilter
    #form = forms.SiteBulkEditForm
    template_name = 'alphalink/cluster_bulk_edit.html'
    default_return_url = 'alphalink:cluster_list'

class ClusterDeleteView(PermissionRequiredMixin, ObjectDeleteView):
    permission_required = 'alphalink.delete_cluster'
    model = Cluster
    default_return_url = 'alphalink:cluster_list'

#
# Resource
#

class ResourceEditView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'dcim.change_device'
    model = Device
    form_class = DeviceForm
    template_name = 'alphalink/resource_edit.html'
    default_return_url = 'alphalink:cluster_list'
