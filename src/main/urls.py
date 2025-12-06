from django.urls import path

from .views import home_view, room_view, create_room_view, update_room_view, delete_room_view

urlpatterns = [
    path('', home_view, name='home'),
    path('room/<str:pk>/', room_view, name='room'),
    path('create-room/', create_room_view, name="create-room"),
    path('update-room/<str:pk>', update_room_view, name="update-room"),
    path('delete-room/<str:pk>', delete_room_view, name="delete-room"),
]
