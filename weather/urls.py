from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.index, name="weather_index"),
    path('<int:pk>/', views.delete, name="delete")
]
