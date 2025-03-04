from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):  # Inherit Django's default UserAdmin
    model = CustomUser
    list_display = ('username', 'email', 'role')
    fieldsets = UserAdmin.fieldsets + (  # Add custom fields to admin panel
        ('Additional Info', {'fields': ('role','confirm_password')}),
    )

# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)