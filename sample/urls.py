# example/urls.py
from django.urls import path

from sample import views
from sample.views import index


urlpatterns = [
    path('', views.hello),
]