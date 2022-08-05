from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from uuid import uuid4

from .utils import upload_path_render, upload_path_panorama, upload_path_imitation_model


class Project(models.Model):
    ''' Model of project '''
    _STATUSES = (('pause', 'pause'), ('in progress', 'in progress'), ('stopped', 'stopped'))

    name = models.CharField("Project's name", max_length=128)
    customer_name = models.CharField("Customer's name", max_length=128)
    customer_phone = models.CharField("Customer's phone", max_length=16)
    customer_email = models.CharField("Customer's email", max_length=128)
    start_date = models.DateTimeField("Start date", null=True, default=datetime.now)
    end_date = models.DateTimeField("End date", null=True)
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField("Project's status", max_length=64, choices=_STATUSES, default=_STATUSES[0][0])
    ready = models.IntegerField("Project's readiness", default=0)
    code = models.UUIDField("Project's code", primary_key=True, default=uuid4, editable=False)
    imitation_model = models.FileField(upload_to=upload_path_imitation_model, null=True)


class Room(models.Model):
    ''' Room of project '''
    _STATUSES = (('agreed', 'agreed'), ('disagreed', 'disagreed'))

    name = models.CharField("Room's name", max_length=128)
    status = models.CharField("Room's status", max_length=32, choices=_STATUSES, default=_STATUSES[1][0])
    project = models.ForeignKey(Project, related_name='rooms', on_delete=models.CASCADE)


class RoomRender(models.Model):
    ''' Render for room '''

    room = models.ForeignKey(Room, related_name='renders', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path_render)


class RoomPanorama(models.Model):
    ''' Panorama for room '''

    room = models.ForeignKey(Room, related_name='panoramas', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path_panorama)






