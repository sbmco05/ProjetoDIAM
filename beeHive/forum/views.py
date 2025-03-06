from django.shortcuts import get_object_or_404, render
from .models import Utilizador, User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from topic.models import Topic
from post.models import Post, Like
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test, login_required




# Create your views here.
def base(request):
    topicos = Topic.objects.all()
    context = {'topicos': topicos}
    return render(request, 'forum/base.html', context)

def dologin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('forum:index'))
        else:
            return render(request, 'forum/Login.html', {'msg_erro':"Username ou password inválido"})
    else:
        return render(request, 'forum/Login.html')

def index(request):
    topicos = Topic.objects.all()
    latest_posts = Post.objects.order_by('created_at').reverse()[:10]
    context = {'latest_posts': latest_posts, 'topicos': topicos}
    return render(request, 'forum/index.html', context)

def registo(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        date = request.POST.get('date')

        if not (username and password and email and date):
            return render(request, 'forum/registo.html', {'msg_erro': 'Por favor, preencha todos os campos.'})

        # Verifica se já existe um usuário com o mesmo nome de usuário ou email
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return render(request, 'forum/registo.html', {'msg_erro': 'Nome de usuário ou email já está em uso.'})

        else:
            u = User.objects.create_user(username=username, password=password, email=email)
            u.date = date
            u.save()
            a = Utilizador(username=u)
            a.save()
            return HttpResponseRedirect(reverse('forum:index'))
    else:
        return render(request, 'forum/registo.html')

@login_required(login_url='login/')
def ver_perfil(request):
    user = request.user
    posts = Post.objects.filter(autor=user)
    context = {
        'user': user,
        'posts': posts,
    }
    return render(request, 'forum/perfil.html', context)



def fazlogout(request):
    logout(request)

    topicos = Topic.objects.all()
    latest_posts = Post.objects.order_by('created_at').reverse()[:10]

    context = {'latest_posts': latest_posts, 'topicos': topicos}

    return render(request, 'forum/index.html', context)