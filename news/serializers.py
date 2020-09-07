from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'uid', 'title', 'body', 'url', 'newspaper_uid', 'host')

        model = News
    
    