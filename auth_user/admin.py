from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,OTP

class CustomUserAdmin(UserAdmin):  # Inherit Django's default UserAdmin
    model = CustomUser
    list_display = ('username', 'email', 'role')
    fieldsets = UserAdmin.fieldsets + (  # Add custom fields to admin panel
        ('Additional Info', {'fields': ('role','confirm_password')}),
    )
class OTPAdmin(admin.ModelAdmin):  # Inherit Django's default UserAdmin
    model = OTP
    list_display = ('user','otp','created_at')
# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(OTP,OTPAdmin)