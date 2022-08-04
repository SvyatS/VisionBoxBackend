from django.urls import path

from . import views

CRUD_METHODS_LIST = {'get': 'list', 'post': 'create'}
CRUD_METHODS_ITEM = {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}
CRUD_METHODS_CREATE = {'post': 'create'}

urlpatterns = [
    path('', views.ProjectAPIView.as_view(CRUD_METHODS_LIST), name='project-list'),
    path('<slug:code>', views.ProjectAPIView.as_view(CRUD_METHODS_ITEM), name='project-obj'),
    path('room/render-upload', views.RoomRenderViewset.as_view(CRUD_METHODS_CREATE), name='room-render-upload'),
    path('room/panorama-upload', views.RoomPanoramaViewset.as_view(CRUD_METHODS_CREATE), name='room-panorama-upload'),
]
