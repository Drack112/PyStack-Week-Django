from django.urls import path

from .views import pacientes

urlpatterns = [path("pacientes", pacientes, name="pacientes")]
