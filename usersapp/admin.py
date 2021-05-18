from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('handle_name','phonenumber','status')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    #管理サイトから追加するときのフォーム
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',"handle_name","phonenumber",'status'),
        }),
    )


    list_display = ('email', 'email', 'handle_name','phonenumber', 'status', 'is_staff')
    search_fields = ('email', 'handle_name', 'phonenumber','status')
    #username to Email
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)