from django.conf.urls import url

from ipam.views import ServiceEditView
from secrets.views import secret_add

from . import views


urlpatterns = [

    # ClusterAlpha
    url(r'^cluster_alpha/$', views.ClusterAlphaListView.as_view(), name='cluster_alpha_list'),
    url(r'^cluster_alpha/add/$', views.ClusterAlphaEditView.as_view(), name='cluster_alpha_add'),
    url(r'^cluster_alpha/(?P<slug>[\w-]+)/$', views.cluster_alpha, name='cluster_alpha'),
    url(r'^cluster_alpha/(?P<slug>[\w-]+)/edit/$', views.ClusterAlphaEditView.as_view(), name='cluster_alpha_edit'),
    url(r'^cluster_alpha/(?P<slug>[\w-]+)/delete/$', views.ClusterAlphaDeleteView.as_view(), name='cluster_alpha_delete'),
    url(r'^cluster_alpha/edit/$', views.ClusterAlphaBulkEditView.as_view(), name='cluster_alpha_bulk_edit'),

    # Resource
    url(r'^resource/add/(?P<comments>[\w-]+)', views.ResourceEditView.as_view(), name='cluster_alpha_add_resource'),

]
