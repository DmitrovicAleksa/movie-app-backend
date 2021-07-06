from .models import Movie
from rest_framework import permissions
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class MovieList(APIView):
    queryset = Movie.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = MovieSerializer

    def get(self, request):
        movie = MovieSerializer(request.movie)
        return Response(movie.data)
