from django.shortcuts import render
from .models import Topic
from post.models import Post, Like
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required


def hpage(request, Topic_id):
    topic = get_object_or_404(Topic, pk=Topic_id)
    posts = Post.objects.filter(topic_id=Topic_id).order_by('created_at').reverse()
    user = request.user
    Blike = False
    if user is int:
        likes = Like.objects.filter(user=user)
        Blike = likes.exists()
    context = {'topic': topic, 'posts': posts, 'Blike':Blike}
    return render(request, 'topic/hpage.html', context)

@login_required(login_url='/beeHive/login/')
def new_topic(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        admin = request.user

        if (title and description):
            topic = Topic(title=title, description=description, admin=admin)
            topic.save()
            return HttpResponseRedirect(reverse('forum:index'))
    else:
        return render(request,'topic/new_topic.html')

@login_required(login_url='/beeHive/login/')
def fazer_upload(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    context = {'topic': topic}
    if request.user.username == topic.admin.username:
        if request.method == 'POST' and request.FILES['myfile'] is not None:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            nome_ficheiro = fs.save(myfile.name, myfile)
            url_ficheiro = fs.url(nome_ficheiro)

            topic.banner = nome_ficheiro
            topic.save()

            context = {'topic': topic, 'url_ficheiro': url_ficheiro}

            return render(request, 'topic/fazer_upload.html', context)

        return render(request, 'topic/fazer_upload.html', context)

@login_required(login_url='/beeHive/login/')
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    topic.delete()
    return HttpResponseRedirect(reverse('forum:index'))

@login_required(login_url='/beeHive/login/')
def alterar_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    context = {'topic': topic}
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        if (title):
            topic.title = title
        if (description):
            topic.description = description
        topic.save()
        return HttpResponseRedirect(reverse('topic:hpage', args=(topic_id,)))
    else:
        return render(request,'topic/alterar_topic.html', context)
