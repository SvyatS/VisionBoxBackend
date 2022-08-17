from django.urls import path

from . import views

CRUD_METHODS_LIST = {'get': 'list', 'post': 'create'}
CRUD_METHODS_ITEM = {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}
CRUD_METHODS_CREATE = {'post': 'create'}
CRUD_METHODS_FULL = {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'post': 'create'}

urlpatterns = [
    path('projects/', views.ProjectAPIView.as_view(CRUD_METHODS_LIST), name='project-list'),
    path('projects/<slug:code>', views.ProjectAPIView.as_view(CRUD_METHODS_ITEM), name='project-obj'),
    path('rooms/', views.RoomAPIView.as_view(CRUD_METHODS_CREATE), name='rooms-list'),
    path('rooms/<int:pk>', views.RoomAPIView.as_view(CRUD_METHODS_ITEM), name='room-obj'),
    path('rooms/render/<int:id>', views.RoomRenderViewset.as_view(CRUD_METHODS_FULL), name='room-render-upload'),
    path('rooms/panorama/<int:id>', views.RoomPanoramaViewset.as_view(CRUD_METHODS_FULL), name='room-panorama-upload'),
]
