from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Room, Project


@receiver(post_save, sender=Room)
def project_readiness(sender, **kwargs):
    print("Room was saved")
