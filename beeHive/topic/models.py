from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    banner = models.ImageField(upload_to='banner_topicos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    seguidores = models.IntegerField(default=0)
