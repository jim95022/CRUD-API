from django.conf.urls import url

from .views import UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet)
urlpatterns = router.urls