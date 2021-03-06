from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from authentication.jwtauthenticate import JWTAuthentication

from authentication.serializers import LoginSerializer, RegisterSerializer


class AuthUserAPIView(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response({ 'user': serializer.data })
class RegisterView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)  
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(GenericAPIView):
    
    serializer_class = LoginSerializer
    def post(self, request):

        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer=self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message":"Invalid credentials, try agian..."}, status=status.HTTP_401_UNAUTHORIZED)

        

