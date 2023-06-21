# Django
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.core.exceptions import ValidationError
from django.db import models

# First party
from abstracts.models import AbstractTrackingModel


class CustomUserManager(BaseUserManager):

    def create_user(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':

        if not email:
            raise ValidationError('Email required')

        client: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        client.set_password(password)
        client.save(using=self._db)
        return client

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':

        client: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        client.is_staff = True
        client.is_superuser = True
        client.set_password(password)
        client.save(using=self._db)
        return client


class CustomUser(AbstractBaseUser, PermissionsMixin, AbstractTrackingModel):
    """CustomUser."""

    id: int = models.BigAutoField(
        primary_key=True
    )
    email: str = models.EmailField(
        max_length=100, unique=True, verbose_name='email'
    )
    name: str = models.CharField(
        max_length=50, default='', verbose_name='name'
    )
    surname: str = models.CharField(
        max_length=50, default='', verbose_name='surname'
    )
    is_superuser: bool = models.BooleanField(
        default=False, verbose_name='is superuser'
    )
    is_staff: bool = models.BooleanField(
        default=False, verbose_name='is staff'
    )
    is_active: bool = models.BooleanField(
        default=True, verbose_name='is active'
    )
    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: list[str] = []

    objects = CustomUserManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = 'custom user'
        verbose_name_plural = 'custom users'

    @property
    def fullname(self) -> str:
        return f'{self.name} {self.surname}'
