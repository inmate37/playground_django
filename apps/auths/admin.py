# Python
from typing import Optional

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.handlers.wsgi import WSGIRequest

# Local
from .forms import (
    CustomUserChangeForm,
    CustomUserCreationForm
)
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    fieldsets = (
        ('Information', {
            'fields': (
                'email',
                'name',
                'surname',
                'password',
                'dt_created',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )
    # NOTE: Used to define the fields that
    #       will be displayed on the create-user page
    #
    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'email',
                'password1',
                'password2',
            ),
        }),
    )
    search_fields = (
        'email',
    )
    readonly_fields = (
        'dt_created',
        'is_active',
        'is_staff',
        'is_superuser',
        'name',
        'surname',
    )
    list_display = (
        'email',
        'dt_created',
        'last_login',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
    )
    ordering = (
        '-dt_created',
    )

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[CustomUser] = None
    ) -> tuple:
        if not obj:
            return self.readonly_fields

        return self.readonly_fields + (
            'email',
        )
