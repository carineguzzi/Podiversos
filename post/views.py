from django.shortcuts import render
from django.http import HttpResponse
from .temp_data import post_data

def detail_post(request, post_id):
    post = post_data[post_id - 1]
    return HttpResponse(
        f'Detalhes do Podcast {post["name"]} ({post["release_year"]})')
def list_post(request):
    context = {"post_list": post_data}
    return render(request, 'post/index.html', context)

def detail_post(request, post_id):
    context = {'post': post_data[post_id - 1]}
    return render(request, 'post/detail.html', context)

def create_post(request):
    if request.method == 'POST':
        post_data.append({
            'name': request.POST['name'],
            'release_year': request.POST['release_year'],
            'poster_url': request.POST['poster_url']
        })
        return HttpResponseRedirect(
            reverse('post:detail', args=(len(post_data), )))
    else:
        return render(request, 'post/create.html', {})