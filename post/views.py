from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .temp_data import post_data
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def list_post(request):
    context = {"post_list": post_data}
    return render(request, 'post/index.html', context)

def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'post/detail.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_name = form.cleaned_data['name']
            post_release_year = form.cleaned_data['release_year']
            post_poster_url = form.cleaned_data['poster_url']
            post = Post(name=post_name,
                          release_year=post_release_year,
                          poster_url=post_poster_url)
            post.save()
            return HttpResponseRedirect(
                reverse('post:detail', args=(post.id, )))
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'post/create.html', context)


def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.name = form.cleaned_data['name']
            post.release_year = form.cleaned_data['release_year']
            post.poster_url = form.cleaned_data['poster_url']
            post.save()
            return HttpResponseRedirect(
                reverse('post:detail', args=(post.id, )))
    else:
        form = PostForm(
            initial={
                'name': post.name,
                'release_year': post.release_year,
                'poster_url': post.poster_url
            })

    context = {'post': post, 'form': form}
    return render(request, 'post/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('post:index'))

    context = {'post': post}
    return render(request, 'post/delete.html', context)
