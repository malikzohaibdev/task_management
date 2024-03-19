from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Custom fields
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.EmailField(unique=True)

    # Specify related_name for groups and user_permissions
    groups_related_name = "customuser_groups"
    user_permissions_related_name = "customuser_user_permissions"

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name=groups_related_name,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name=user_permissions_related_name,
        help_text='Specific permissions for this user.',
    )

    class Meta:
        db_table = "user"
        verbose_name = 'User'
        verbose_name_plural = 'Users'

