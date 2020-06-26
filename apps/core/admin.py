from django.contrib import admin
from django.contrib.auth.models import User,Group


#TIRA USUÁRIO E GRUPO DO ADMIN
admin.site.unregister(User)
admin.site.unregister(Group)

#PERSONALIZANDO ADMIN
admin.site.site_header = 'TodoApp Login'
admin.site.site_title = 'Administração TodoApp'
admin.site.index_title = 'Administração TodoApp - Aplicações'
