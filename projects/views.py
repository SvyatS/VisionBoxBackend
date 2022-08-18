from rest_framework import viewsets, parsers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from . import models
from . import serializers
from .models import Project


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


class GetProjectMobile(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, project_code, designer_id):
        queryset = Project.objects.get(code=project_code, editor_id=designer_id)
        serializer = serializers.getProjectMobileSerializer(queryset)
        return Response(serializer.data)
