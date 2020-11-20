from django.urls import path

from .views import (
    all_members_view,
    detail_team_member_view,
    create_team_member_view,
    update_team_member_view,
    delete_team_member_view
)

app_name = 'api'


urlpatterns = [
    path('', all_members_view, name='all_members'),
    path('create/', create_team_member_view, name='create'),
    path('<slug>/', detail_team_member_view, name='detail'),
    path('<slug>/update', update_team_member_view, name='update'),
    path('<slug>/delete', delete_team_member_view, name='delete')
]