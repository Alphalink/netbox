import re

from mptt.forms import TreeNodeChoiceField

from django import forms
from django.contrib.postgres.forms.array import SimpleArrayField
from django.core.exceptions import ValidationError
from django.db.models import Count, Q

from extras.forms import CustomFieldForm, CustomFieldBulkEditForm, CustomFieldFilterForm
from ipam.models import IPAddress
from tenancy.models import Tenant
from utilities.forms import (
    APISelect, add_blank_choice, ArrayFieldSelectMultiple, BootstrapMixin, BulkEditForm, BulkImportForm, CommentField,
    CSVDataField, ExpandableNameField, FilterChoiceField, FlexibleModelChoiceField, Livesearch, SelectWithDisabled,
    SmallTextarea, SlugField, FilterTreeNodeMultipleChoiceField,
)

from .formfields import MACAddressFormField
from .models import (
    Cluster
)


FORM_STATUS_CHOICES = [
    ['', '---------'],
]

#FORM_STATUS_CHOICES += STATUS_CHOICES

#
# Clusters
#

class ClusterForm(BootstrapMixin, forms.ModelForm):

    comments = CommentField()
    slug = SlugField()

    class Meta:
        model = Cluster
        fields = ['name','slug','comments','memory','cpu']

    def __init__(self, *args, **kwargs):

        super(ClusterForm, self).__init__(*args, **kwargs)
