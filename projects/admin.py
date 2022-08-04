from django.contrib import admin

from . import models


class RoomRenderInline(admin.TabularInline):
    model = models.RoomRender
    extra = 3

class RoomPanoramaInline(admin.TabularInline):
    model = models.RoomPanorama
    extra = 3

class RoomAdmin(admin.ModelAdmin):
    inlines = [ RoomRenderInline, RoomPanoramaInline ]

admin.site.register(models.Project)
admin.site.register(models.Room, RoomAdmin)
