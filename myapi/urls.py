from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from myapi.main_page import views 

from myapi.core.views import registration_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_main_page),
    path('register/', registration_view, name='register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/', include('myapi.core.urls'), name='api')
]
