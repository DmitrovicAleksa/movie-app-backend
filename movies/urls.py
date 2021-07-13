from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include
from django.conf.urls import url



router = DefaultRouter()
router.register(r'movies', views.MovieList, basename="users")
router.register(r'genres', views.GenreList, basename="genres")


urlpatterns = [
    url('',include(router.urls)),
]