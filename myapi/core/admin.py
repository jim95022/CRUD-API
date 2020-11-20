from django.contrib import admin
from myapi.core.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class CoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'inner_username', 'role', 'is_active')
    list_display_links = ('inner_username',)
    search_fields = ('inner_username',)


admin.site.register(TeamMember, CoreAdmin)