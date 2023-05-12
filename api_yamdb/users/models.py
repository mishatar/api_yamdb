from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

ROLES = (('user', 'юзер'), ('moderator', 'модератор'), ('admin', 'админ'),)
USER = 'user'


def validate_username_me(username):
    if username == 'me':
        raise ValidationError('Нельзя использовать me')


class CustomUser(AbstractUser):
    username = models.TextField(
        'username',
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+\Z',
                message='Неверно введено имя'
            ), validate_username_me]
    )
    email = models.EmailField(
        'email',
        unique=True,
        max_length=254,
        blank=False,
        null=False,
    )
    first_name = models.TextField(
        'name',
        blank=True,
        max_length=150
    )
    last_name = models.TextField(
        'last_name',
        blank=True,
        max_length=150
    )
    bio = models.TextField(
        'Биография',
        blank=True,
        null=True,
        max_length=1000
    )
    role = models.CharField(
        choices=ROLES,
        default=USER,
        max_length=50
    )

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser
