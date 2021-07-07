from .models import Movie
from rest_framework import permissions
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import viewsets


class MovieList(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MovieSerializer