from django.db import models

# Create your models here.
from django.db import models
from topic.models import Topic
from forum.models import Utilizador
from django.contrib.auth.models import User

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default=1)
    title = models.TextField(default="Sem título")
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
