from django.conf.urls import url

from ipam.views import ServiceEditView
from secrets.views import secret_add

from . import views


urlpatterns = [

    # Cluster
    url(r'^cluster/$', views.ClusterListView.as_view(), name='cluster_list'),
    url(r'^cluster/add/$', views.ClusterEditView.as_view(), name='cluster_add'),
    url(r'^cluster/(?P<slug>[\w-]+)/$', views.cluster, name='cluster'),
    url(r'^cluster/(?P<slug>[\w-]+)/edit/$', views.ClusterEditView.as_view(), name='cluster_edit'),
    url(r'^cluster/(?P<slug>[\w-]+)/delete/$', views.ClusterDeleteView.as_view(), name='cluster_delete'),
    url(r'^cluster/edit/$', views.ClusterBulkEditView.as_view(), name='cluster_bulk_edit'),

    # Resource
    url(r'^resource/add/(?P<comments>[\w-]+)', views.ResourceEditView.as_view(), name='cluster_add_resource'),

]
