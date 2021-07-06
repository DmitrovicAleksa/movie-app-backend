from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include


router = DefaultRouter()
router.register(r'movies', views.MovieList, basename="movies")


urlpatterns = [
    url('',include(router.urls)),
]