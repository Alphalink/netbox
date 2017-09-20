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

# ClusterAlphas
router.register(r'cluster_alphas', views.ClusterAlphaViewSet)

app_name = 'alphalink-api'
urlpatterns = router.urls
