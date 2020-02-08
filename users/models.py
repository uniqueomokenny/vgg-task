from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from rest_framework.authtoken.models import Token
from django.db import transaction


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Username is a required field.')

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=120, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'username'

    objects = UserManager()

    def save(self, *args, **kwargs):

        with transaction.atomic():
            super().save(*args, **kwargs)
            Token.objects.get_or_create(user=self)

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username', )
