from django.urls import path

from authentication.views import (RegisterView, LoginAPIView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name="login")
]