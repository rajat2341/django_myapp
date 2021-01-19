from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from authentication.models import User, UserDetails

admin.site.register(UserDetails)

@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ["id", "username", "first_name", "last_name", "email", "role", "relation"]
    list_filter = ["id", "username", "role"]
