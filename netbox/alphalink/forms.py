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
    APISelect, add_blank_choice, ArrayFieldSelectMultiple, BootstrapMixin, BulkEditForm, CommentField,
    CSVDataField, ExpandableNameField, FilterChoiceField, FlexibleModelChoiceField, Livesearch, SelectWithDisabled,
    SmallTextarea, SlugField, FilterTreeNodeMultipleChoiceField,
)

from .formfields import MACAddressFormField
from .models import (
    ClusterAlpha
)


FORM_STATUS_CHOICES = [
    ['', '---------'],
]

#FORM_STATUS_CHOICES += STATUS_CHOICES

#
# ClusterAlphas
#

class ClusterAlphaForm(BootstrapMixin, forms.ModelForm):

    comments = CommentField()
    slug = SlugField()

    class Meta:
        model = ClusterAlpha
        fields = ['name','slug','comments','memory','cpu']

    def __init__(self, *args, **kwargs):

        super(ClusterAlphaForm, self).__init__(*args, **kwargs)
