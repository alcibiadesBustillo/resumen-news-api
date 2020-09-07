from django.contrib.auth import get_user_model
#from rest_framework import generics, permissions
from rest_framework import viewsets

from .models import News
from .permissions import IsAuthorOrReadOnly
from .serializers import NewsSerializer, UserSerializer

# Create your views here.

# class NewsList(generics.ListCreateAPIView):
#     #permission_classes = (permissions.IsAuthenticated,) # View-Level Permissions    
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer

# class NewsDetail(generics.RetrieveUpdateDestroyAPIView): # generics.RetrieveAPIView just view 
#     #permission_classes = (permissions.IsAuthenticated,) # View-Level Permissions
#     #permission_classes = (IsAuthorOrReadOnly,)
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# Creating viewsets

class NewsViewSet(viewsets.ModelViewSet):
    #permission_classes = (IsAuthorOrReadOnly,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given user.

    list:
    Return a list of all the existing users.

    create:
    Create a new user instance.
    """
    #permission_classes = (IsAuthorOrReadOnly,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
