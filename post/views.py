from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .temp_data import post_data
from django.shortcuts import render, get_object_or_404

def list_post(request):
    context = {"post_list": post_data}
    return render(request, 'post/index.html', context)

def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'post/detail.html', context)

def create_post(request):
    if request.method == 'POST':
        post_name = request.POST['name']
        post_release_year = request.POST['release_year']
        post_poster_url = request.POST['poster_url']
        post = Post(name=post_name,
                      release_year=post_release_year,
                      poster_url=post_poster_url)
        post.save()
        return HttpResponseRedirect(
            reverse('post:detail', args=(post.id, )))
    else:
        return render(request, 'post/create.html', {})
def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.name = request.POST['name']
        post.release_year = request.POST['release_year']
        post_poster_url = request.POST['poster_url']
        post.save()
        return HttpResponseRedirect(
            reverse('post:detail', args=(post.id, )))

    context = {'post': post}
    return render(request, 'post/update.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse('post:index'))

    context = {'post': post}
    return render(request, 'post/delete.html', context)
