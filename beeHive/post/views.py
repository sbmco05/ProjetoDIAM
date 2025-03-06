from django.shortcuts import render
from .models import Post,Comment,Like
from django.shortcuts import get_object_or_404, render, redirect
from topic.models import Topic
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required(login_url='/beeHive/login/')
def new_post(request, topic_id):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('file', None)
        autor = request.user
        topic = get_object_or_404(Topic, pk=topic_id)

        if (title and content):
            post = Post(topic=topic, title=title, content=content, image=image, autor=autor)
            post.save()
            context ={'topic':topic, 'post':post}
            return render(request, 'post/Post_page.html', context)
    else:
        topic = get_object_or_404(Topic, pk=topic_id)
        return render(request, 'post/new_post.html', {'topic': topic})

def post_page(request, topic_id, post_id):
    post = get_object_or_404(Post, pk=post_id)
    topic = get_object_or_404(Topic, pk=topic_id)
    comments = Comment.objects.filter(post_id=post_id)
    context = {'topic': topic, 'post': post, 'comments': comments}
    if (request.user.is_authenticated):
        likes = Like.objects.filter(user=request.user, post=post)
        context = {'topic': topic, 'post': post, 'comments': comments, 'likes' : likes}
    return render(request, 'post/post_page.html', context)

@login_required(login_url='/beeHive/login/')
def new_comment(request, topic_id, post_id):
    content = request.POST['content']
    autor = request.user
    post = get_object_or_404(Post, pk=post_id)
    if (content):
        comment = Comment(post=post, content=content, autor=autor)
        comment.save()
        return HttpResponseRedirect(reverse('post:post_page', args=(topic_id,post_id)))
    return
@login_required(login_url='/beeHive/login/')
def alterar_post(request, topic_id, post_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    post = get_object_or_404(Post, pk=post_id)
    context = {'topic': topic, 'post': post}
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        if (title):
            post.title = title
        if (content):
            post.content = content

        post.save()

        return HttpResponseRedirect(reverse('post:post_page', args=(topic_id,post_id,)))
    else:
        return render(request, 'post/alterar_post.html', context)

@login_required(login_url='/beeHive/login/')
def post_upload(request, topic_id, post_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    post = get_object_or_404(Post, pk=post_id)
    context = {'topic': topic, 'post': post}
    if request.method == 'POST' and request.FILES['myfile'] is not None:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        nome_ficheiro = fs.save(myfile.name, myfile)
        url_ficheiro = fs.url(nome_ficheiro)

        post.image = nome_ficheiro
        post.save()

        context = {'topic': topic, 'post': post, 'url_ficheiro': url_ficheiro}

        return render(request, 'post/upload_post.html', context)

    return render(request, 'post/upload_post.html', context)

@login_required(login_url='/beeHive/login/')
def delete_post(request, topic_id, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('topic:hpage', args=(topic_id,)))

@login_required(login_url='/beeHive/login/')
def like_post(request, post_id, topic_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    isliked= Like.objects.filter(user=user, post=post)
    for like in isliked:
        if like.post.id == post_id and like.user == user:
            return HttpResponseRedirect(reverse('post:post_page', args=(topic_id,post_id)))
    like = Like(user=user, post=post)
    post.likes += 1
    post.save()
    like.save()
    return HttpResponseRedirect(reverse('post:post_page', args=(topic_id, post_id)))

@login_required(login_url='/beeHive/login/')
def dislike_post(request, post_id, topic_id):
    post = get_object_or_404(Post, pk=post_id)
    like = Like.objects.filter(user=request.user)
    post.likes -= 1
    post.save()
    like.delete()
    return HttpResponseRedirect(reverse('post:post_page', args=(topic_id, post_id)))
