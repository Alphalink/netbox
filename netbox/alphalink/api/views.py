from rest_framework.viewsets import ModelViewSet

from alphalink.models import Cluster
from alphalink.filters import ClusterFilter

from extras.api.views import CustomFieldModelViewSet
from utilities.api import WritableSerializerMixin
from . import serializers


#
# Cluster
#

class ClusterViewSet(ModelViewSet):
    queryset = Cluster.objects.all()
    serializer_class = serializers.ClusterSerializer
    write_serializer_class = serializers.WritableClusterSerializer
    filter_class = ClusterFilter
