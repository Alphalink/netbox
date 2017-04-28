from rest_framework import routers

from . import views


class AlphalinkRootView(routers.APIRootView):
    """
    Alphalink API root view
    """
    def get_view_name(self):
        return 'Alphalink'


router = routers.DefaultRouter()
router.APIRootView = AlphalinkRootView

# Clusters
router.register(r'clusters', views.ClusterViewSet)

app_name = 'alphalink-api'
urlpatterns = router.urls
