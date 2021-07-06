from .models import Movie
from rest_framework import viewsets,permissions
from .serializers import MovieSerializer


class MovieList(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MovieSerializer