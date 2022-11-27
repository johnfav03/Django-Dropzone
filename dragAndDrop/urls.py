from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display/', views.display, name='display'),
    path('upload/', views.upload_file),
    path('display/clear/', views.display_clear, name='clear'),
]