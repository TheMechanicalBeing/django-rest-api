from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ("email", "is_staff", "is_active", "is_superuser", "is_author", "bio")
    list_filter = ("is_staff", "is_active", "is_superuser", "user_permissions")

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ("Author", {'fields': ("is_author", "bio", "profile_picture")}),
        ("Permissions", {'fields': ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (
            None, {
                "classes": ("wide",),
                "fields": (
                    "email", "password1", "password2", "is_staff",  "is_active", "groups", "user_permissions"
                )
            }
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
