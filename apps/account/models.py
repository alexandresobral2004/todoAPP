from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    photo = models.ImageField('Foto', upload_to='photos')
    cell_phone = models.CharField('Celular', max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
       verbose_name = 'Perfil do Usuário'
       verbose_name_plural = 'Perfis dos Usuários'
       
    
    def __str__(self):
      return self.user.username