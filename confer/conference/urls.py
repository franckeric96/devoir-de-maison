from django.urls import path
from . import views

urlpatterns = [
    path('speakers', views.speaker, name='speaker'),
    path('schedule', views.schedule, name='schedule'),
    path('tickets', views.ticket, name='ticket'),
]