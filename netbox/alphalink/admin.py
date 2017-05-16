from django.contrib import admin
from django.db.models import Count

from mptt.admin import MPTTModelAdmin

from .models import (
    Cluster,
)


@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'memory', 'cpu']
    prepopulated_fields = {
        'slug': ['name'],
    }
