#views

from django.shortcuts import render, redirect

from galeria.models import Post

from galeria.forms import PostForms

from django.contrib import messages



def  index(request):
    return render(request, 'galeria/index.html')

def card(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    posts = Post.objects.filter(privacidade=True)
    context = {'posts': posts}
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
