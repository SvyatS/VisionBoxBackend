from django.db import models
from datetime import datetime
from uuid import uuid4

from users.models import CustomUser
from .utils import upload_path_render, upload_path_panorama, upload_path_imitation_model
from users.utils import id_generator


class Project(models.Model):
    ''' Model of project '''
    _STATUSES = (('pause', 'pause'), ('in progress', 'in progress'), ('stopped', 'stopped'))

    name = models.CharField("Project's name", max_length=128)
    customer_name = models.CharField("Customer's name", max_length=128)
    customer_phone = models.CharField("Customer's phone", max_length=16)
    customer_email = models.CharField("Customer's email", max_length=128)
    start_date = models.DateTimeField("Start date", null=True, default=datetime.now)
    end_date = models.DateTimeField("End date", null=True)
    editor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField("Project's status", max_length=64, choices=_STATUSES, default=_STATUSES[0][0])
    ready = models.IntegerField("Project's readiness", default=0)
    code = models.CharField("Project's code", max_length=8, primary_key=True, default=id_generator, editable=False)
    imitation_model = models.FileField(upload_to=upload_path_imitation_model, null=True, blank=True)


class Room(models.Model):
    ''' Room of project '''
    _STATUSES = (('agreed', 'agreed'), ('disagreed', 'disagreed'))

    name = models.CharField("Room's name", max_length=128)
    status = models.CharField("Room's status", max_length=32, choices=_STATUSES, default=_STATUSES[1][0])
    project = models.ForeignKey(Project, related_name='rooms', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Room, self).save(*args, **kwargs)
        if getattr(self, 'status_changed', True):
            project = Project.objects.get(code=self.project_id)
            agreed_rooms = project.rooms.filter(status=self._STATUSES[0][0]).count()
            project.ready = agreed_rooms * 100 / project.rooms.count()
            project.save()


class RoomRender(models.Model):
    ''' Render for room '''

    room = models.ForeignKey(Room, related_name='renders', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path_render)


class RoomPanorama(models.Model):
    ''' Panorama for room '''

    room = models.ForeignKey(Room, related_name='panoramas', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path_panorama)






