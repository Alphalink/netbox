import django_filters
from netaddr.core import AddrFormatError

from django.db.models import Q

from extras.filters import CustomFieldFilterSet
from tenancy.models import Tenant
from utilities.filters import NullableModelMultipleChoiceFilter
from .models import (
    ClusterAlpha,
)

class ClusterAlphaFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )

    class Meta:
        model = ClusterAlpha
        fields = ['q', 'name']

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        qs_filter = (
            Q(name__icontains=value) |
            Q(comments__icontains=value)
        )
        try:
            qs_filter |= Q(asn=int(value.strip()))
        except ValueError:
            pass
        return queryset.filter(qs_filter)
