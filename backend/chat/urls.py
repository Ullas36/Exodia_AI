from django.urls import path
from .views import chat,reset

urlpatterns = [
    path('chat/', chat),
    path('reset/',reset)
]
