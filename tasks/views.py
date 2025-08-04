from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets, filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Task
from .serializers import TaskSerializer
from .serializers import RegistrationSerializer
from .serializers import MyTokenObtainPairSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes     = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('completed',)
    search_fields    = ('title', 'description')

class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response({
            'user': {
                'id':       user.id,
                'username': user.username,
                'email':    user.email,
            },
            'access':  access_token,
            'refresh': refresh_token,
        }, status=status.HTTP_201_CREATED)
    
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer