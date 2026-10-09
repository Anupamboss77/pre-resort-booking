from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'rooms/',
        views.rooms,
        name='rooms'
    ),

    path(
        'booking/',
        views.booking_form,
        name='booking'
    ),

    path(
        'confirmation/<int:booking_id>/',
        views.confirmation,
        name='confirmation'
    ),
]