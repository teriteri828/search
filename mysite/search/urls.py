from django.urls import path

from .views import application_controller

app_name = 'search'
urlpatterns = [
    path('', application_controller.index, name='index'),
    path('result', application_controller.search, name='search'),
]