from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    email_active_code = models.CharField(max_length=128, unique=True, verbose_name='کد فعالسازی')
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^09\d{9}$',
            )
        ],
        verbose_name='شماره تلفن'
    )
    is_author = models.BooleanField(default=False, verbose_name='نویسنده')