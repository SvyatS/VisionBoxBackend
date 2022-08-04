from requests import Response
from rest_framework import viewsets, parsers

from . import models
from . import serializers


class ProjectAPIView(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    lookup_field = 'code'


class RoomRenderViewset(viewsets.ModelViewSet):
    serializer_class = serializers.RoomRenderSerializer
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser)
    queryset = models.RoomRender.objects.all()
    lookup_field = 'id'


class RoomPanoramaViewset(viewsets.ModelViewSet):
    serializer_class = serializers.RoomPanoramaSerializer
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser)
    queryset = models.RoomPanorama.objects.all()
    lookup_field = 'id'
