from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Custom fields
    phone = models.CharField(max_length=30, blank=True, null=True)

    # Override groups and user_permissions with custom related_names
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'




