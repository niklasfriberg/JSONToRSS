from django.urls import path
from . import views

urlpatterns = [
    path('polisen.xml', views.serve_polisen_xml, name='serve_polisen_xml'),
]