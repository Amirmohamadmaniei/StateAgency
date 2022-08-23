from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserCreationForm, UserChangeForm


class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = CustomUser

    list_display = ('phone', 'is_admin')
    list_filter = ('is_admin', 'is_admin')
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        ('Personal info',
         {'fields': ('first_name', 'last_name', 'image')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'phone', 'password1', 'password2', 'first_name', 'last_name', 'is_admin', 'is_active', 'image'),
        }),
    )
    search_fields = ('phone',)
    ordering = ('phone',)
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.unregister(Group)
