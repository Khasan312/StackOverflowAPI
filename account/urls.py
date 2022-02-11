from django.urls import path

from account.views import RegisterAPIView, ActivateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns =[
    path('register/', RegisterAPIView.as_view()),
    path('activate/', ActivateAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

]
