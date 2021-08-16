# from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, authentication, permissions, filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer, QuestionSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """MAnage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user

class ListAPIView(generics.ListCreateAPIView):
    search_fields = ['name','email']
    filter_backends = (filters.SearchFilter,)
    queryset = get_user_model().objects.all()
    serializer_class = QuestionSerializer
