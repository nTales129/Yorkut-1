#views

from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponseRedirect

from django.urls import reverse

from galeria.models import Post, Comentario

from galeria.forms import PostForms, ComentarioForm

from django.contrib import messages

from django.contrib.auth import get_user_model






def  index(request):
    return render(request, 'galeria/index.html')

def card(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    posts = Post.objects.filter(privacidade=True)
    context = {
        'posts': posts,
        'user': request.user,  
    }
    return render(request, 'galeria/card.html', context)

def postar(request):

    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = PostForms
    if request.method == 'POST':
        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            form.instance.autor = request.user
            form.save()
            messages.success(request, 'Nova post publicado com sucesso!')
            return redirect('card')

    return render(request,'galeria/pages/postar.html', {'form': form})

def editar_post(request):
    pass

def apagar_post(request):
    pass

def verpost(request):
    comentarios = Comentario.objects.all()  
    form = ComentarioForm()

    context = {
        'comentarios': comentarios,
        'form': form,  
    }
    return render(request, 'galeria/pages/ver-post.html', context)

def perfil(request):
    return render(request, 'galeria/pages/perfil.html')

def amigos(request):
    return render(request, 'galeria/pages/amigos.html')

def comentario(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            texto = form.cleaned_data['texto']
            autor = request.user
            Comentario.objects.create(post=post, autor=autor, texto=texto)
            return HttpResponseRedirect(reverse('comentario', args=[post_id]))
    else:
        form = ComentarioForm()

    comentarios = Comentario.objects.filter(post=post)

    context = {
        'post': post,
        'form': form,
        'comentarios': comentarios,
    }
    return render(request, 'seu_template_de_formulario.html', {'form': form})
