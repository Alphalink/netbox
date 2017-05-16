from rest_framework import serializers

from extras.api.customfields import CustomFieldModelSerializer
from alphalink.models import Cluster

#
# Cluster
#

class ClusterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cluster
        fields = ['id', 'name', 'slug', 'cpu', 'memory', 'comments']


class NestedClusterSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='alphalink-api:cluster-detail')

    class Meta:
        model = Cluster
        fields = ['id', 'url', 'name', 'slug']


class WritableClusterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cluster
        fields = ['id', 'name', 'slug', 'cpu', 'memory', 'comments']
