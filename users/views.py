from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets,permissions
from rest_framework.views import APIView

# Create your views here.

class RegisterUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class LoginUserView(APIView):
#     queryset = User.objects.all()
#     permission_classes = [permissions.IsAuthenticated]
#     serilazer_class = UserSerializer
