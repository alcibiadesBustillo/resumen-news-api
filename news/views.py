from rest_framework import generics, permissions

from .models import News
from .permissions import IsAuthorOrReadOnly
from .serializers import NewsSerializer

# Create your views here.

class NewsList(generics.ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,) # View-Level Permissions    
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetail(generics.RetrieveUpdateDestroyAPIView): # generics.RetrieveAPIView just view 
    #permission_classes = (permissions.IsAuthenticated,) # View-Level Permissions
    #permission_classes = (IsAuthorOrReadOnly,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer