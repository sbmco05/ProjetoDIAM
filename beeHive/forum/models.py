from django.db import models
from django.contrib.auth.models import User

# Create your models here.
app_label = 'forum'
class Utilizador(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='fotos_de_perfil/', null=True, blank=True)