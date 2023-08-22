from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .serializers import MyTokenObtainPairSerializer, UserSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

from django.contrib.auth.models import User

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserRegistration(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class AdminGetAllUser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]


class UserDetail(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = self.request.user

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj


class AdminGetUserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

