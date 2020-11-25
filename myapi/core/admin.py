from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from myapi.core.models import TeamMember


class CoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'role', 'wage')
    list_display_links = ('username',)
    search_fields = ('username',)


admin.site.register(TeamMember, CoreAdmin)