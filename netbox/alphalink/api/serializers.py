from rest_framework import serializers

from extras.api.customfields import CustomFieldModelSerializer
from alphalink.models import ClusterAlpha

#
# ClusterAlpha
#

class ClusterAlphaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClusterAlpha
        fields = ['id', 'name', 'slug', 'cpu', 'memory', 'comments']


class NestedClusterAlphaSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='alphalink-api:cluster_alpha-detail')

    class Meta:
        model = ClusterAlpha
        fields = ['id', 'url', 'name', 'slug']


class WritableClusterAlphaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClusterAlpha
        fields = ['id', 'name', 'slug', 'cpu', 'memory', 'comments']
