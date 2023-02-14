from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile

# Register your models here.

class ProfileAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'is_active')
    list_display_links = ('email', 'first_name', 'last')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Profile, ProfileAdmin)
