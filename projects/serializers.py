from abc import ABC

from rest_framework import serializers

from . import models


class RoomImagesSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.image.url


class RoomSerializer(serializers.ModelSerializer):
    renders = RoomImagesSerializer(many=True, read_only=True)
    panoramas = RoomImagesSerializer(many=True, read_only=True)

    class Meta:
        model = models.Room
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, required=False)
    imitation_model = serializers.FileField(required=False)

    class Meta:
        model = models.Project
        fields = '__all__'


class RoomRenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomRender
        fields = '__all__'


class RoomPanoramaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoomPanorama
        fields = '__all__'





