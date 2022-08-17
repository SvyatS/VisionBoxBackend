from rest_framework import viewsets, parsers

from . import models
from . import serializers


class ProjectAPIView(viewsets.ModelViewSet):
    # queryset = get_queryset()
    serializer_class = serializers.ProjectSerializer
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser)
    lookup_field = 'code'

    def get_queryset(self):
        user = self.request.user
        return models.Project.objects.filter(editor=user)


class RoomAPIView(viewsets.ModelViewSet):
    serializer_class = serializers.RoomSerializer
    queryset = models.Room.objects.all()
    parser_classes = (parsers.MultiPartParser, parsers.JSONParser)
    lookup_field = 'pk'


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
