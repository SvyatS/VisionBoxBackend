from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.utils import upload_user_avatar, id_generator


class CustomUser(AbstractUser):
    email = models.EmailField('Email address', max_length=255, null=True, blank=True)
    avatar = models.ImageField(upload_to=upload_user_avatar, null=True, blank=True)
    full_name = models.CharField('Full name', max_length=256)
    phone_number = PhoneNumberField(unique=True, null=True, blank=True)
    id = models.CharField("User's code", unique=True, max_length=8, default=id_generator, editable=False, primary_key=True)

    def str(self):
        return self.username
