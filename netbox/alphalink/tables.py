import django_tables2 as tables
from django_tables2.utils import Accessor

from utilities.tables import BaseTable, ToggleColumn

from .models import (
    ClusterAlpha,
)

UTILIZATION_GRAPH = """
{% load helpers %}
{% utilization_graph value %}
"""

#
# ClusterAlpha
#

class ClusterAlphaTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(verbose_name='Name')
    slug = tables.Column(verbose_name='Slug')

    cpu_utilization = tables.TemplateColumn(UTILIZATION_GRAPH, orderable=False, verbose_name='CPU Utilization')
    ram_utilization = tables.TemplateColumn(UTILIZATION_GRAPH, orderable=False, verbose_name='RAM Utilization')

    class Meta(BaseTable.Meta):
        model = ClusterAlpha
        fields = ('pk', 'name', 'slug', 'memory', 'cpu', 'ram_utilization', 'cpu_utilization')

