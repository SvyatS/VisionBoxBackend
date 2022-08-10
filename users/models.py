from django.db import models
from django.contrib.auth.models import AbstractUser


class Designer(AbstractUser):
    pass


class MobileUser(AbstractUser):
    pass


class DesktopUser(AbstractUser):
    pass

