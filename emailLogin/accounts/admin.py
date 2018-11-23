# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from accounts.models import User, UserFollowedUser
from django.utils.translation import gettext_lazy as _


class UserAdmin(DjangoUserAdmin):
    """
    custom user model
    """
    fieldsets = (
            (None, {'fields':('email', 'password')}),
            (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
            (_('Permissions'), {'fields':('is_active','is_staff','is_superuser', 'groups', 'user_permissions')}),
            (_('Important Dates'), {'fields':('last_login', 'date_joined')}),
            )
    add_fieldsets = (
            (None, {
                'classes':('wide',),
                'fields':('email', 'password1', 'password2'),
                }),
            )
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    search_field = ('email', 'first_name', 'last_name')
    ordering = ('-id',)

admin.site.register(User, UserAdmin)
admin.site.register(UserFollowedUser)
