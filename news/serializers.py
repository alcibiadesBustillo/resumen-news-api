from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'uid', 'title', 'body', 'url', 'newspaper_uid', 'host')

        model = News
    
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)    