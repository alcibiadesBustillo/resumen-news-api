from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    uid = models.UUIDField()
    title = models.CharField(max_length=100)
    body = models.TextField()
    url = models.URLField()
    newspaper_uid = models.CharField(max_length=100)
    host =  models.URLField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'news'