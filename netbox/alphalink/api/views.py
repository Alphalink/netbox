from rest_framework.viewsets import ModelViewSet

from alphalink.models import ClusterAlpha
from alphalink.filters import ClusterAlphaFilter

from extras.api.views import CustomFieldModelViewSet
from utilities.api import WritableSerializerMixin
from . import serializers


#
# ClusterAlpha
#

class ClusterAlphaViewSet(ModelViewSet):
    queryset = ClusterAlpha.objects.all()
    serializer_class = serializers.ClusterAlphaSerializer
    write_serializer_class = serializers.WritableClusterAlphaSerializer
    filter_class = ClusterAlphaFilter
