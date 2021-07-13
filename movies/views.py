from .models import Genre, Movie
from rest_framework import permissions
from .serializers import GenreSerializer, MovieSerializer
from rest_framework import viewsets


class MovieList(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = MovieSerializer


class GenreList(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = GenreSerializer
