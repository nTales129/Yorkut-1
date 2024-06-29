from django.urls import path 
from galeria.views import index, card, postar, editar_post, apagar_post, verpost, perfil, amigos, comentario

urlpatterns = [
    path('', index),
    path('card/', card, name='card'),
    path('postar', postar, name='postar'),
    path('verpost', verpost, name='verpost'),
    path('comentario', comentario, name='comentario'),
    path('editar-post', editar_post, name='editar_post'),
    path('apagar-post', apagar_post, name='apagar_post'),
    path('perfil', perfil, name='perfil'),
    path('amigos', amigos, name='amigos')
]