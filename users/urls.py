from django.urls import path
from users.views import LoginUserView, RegisterUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
]
