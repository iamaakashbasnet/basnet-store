from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Account Information', {
            'fields': (
                ('username', 'password',),
            )
        },),
        (('Personal Information'), {
            'fields': (
                ('first_name', 'last_name',),
            )
        },),
        (('Permissions'), {
            'fields': (
                ('is_active', 'is_staff', 'is_admin', 'is_superuser',),
                'groups',
                'user_permissions',
            ),
            'classes': ('collapse',)
        },),
        (('Important Dates'), {
            'fields': (
                ('date_joined', 'last_login',),
            ),
            'classes': ('collapse',)
        },),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2',),
        },),
    )

    list_display = ('username', 'first_name', 'last_name',)
    ordering = ('username',)
    search_fields = ('username',)
    readonly_fields = ('date_joined', 'last_login',)
