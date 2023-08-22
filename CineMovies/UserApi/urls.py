from django.urls import path
from .views import MyTokenObtainPairView, AdminGetAllUser, UserDetail, AdminGetUserDetail
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/users/', AdminGetAllUser.as_view(), name='admin-get-all-user'),
    path("admin/user/<int:pk>/", AdminGetUserDetail.as_view(), name="admin-get-user-detail"),
    path('user/', UserDetail.as_view(), name='user-detail'),
]