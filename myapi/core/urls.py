from django.conf.urls import url

from .views import UserViewSet


urlpatterns = [
    url(
        r'^$',
        UserViewSet.as_view({'get': 'list'}),
        name='user-list',
    ),
    url(
        r'^(?P<pk>\d+)$',
        UserViewSet.as_view({'get': 'retrieve'}),
        name='user-detail',
    ),
    url(
        r'^create$',
        UserViewSet.as_view({'post': 'create'}),
        name='user-create',
    ),
    url(
        r'^(?P<pk>\d+)/update$',
        UserViewSet.as_view({'put': 'partial_update'}),
        name='user-update',
    ),
    url(
        r'^(?P<pk>\d+)/delete$',
        UserViewSet.as_view({'delete': 'destroy'}),
        name='user-delete',
    ),
]
