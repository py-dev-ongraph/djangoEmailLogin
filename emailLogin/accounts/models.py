# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import time
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import UserManager

class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    email = models.EmailField(_('email_address'), unique=True)
    follower_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.email


class UserFollowedUser(models.Model):
    user = models.ForeignKey(User, related_name='follows', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'user:%s -> user:%s' % (self.user_id, self.following_id)
