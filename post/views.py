from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .temp_data import post_data
from django.urls import reverse, reverse_lazy
from .models import Post, Comment
from django.views import generic
from .forms import PostForm, CommentForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView


class PostListView(generic.ListView):
   post = Post
   template_name = 'post/index.html'


   def get_queryset(self):
       return Post.objects.order_by('id')


class PostDetailView(generic.DetailView):
   post = Post
   template_name = 'post/detail.html'


   def get_queryset(self):
       return Post.objects.all()


class PostCreateView(CreateView):
   form_class = PostForm
   template_name = 'post/create.html'
   success_url = reverse_lazy('post:index')


   def form_valid(self, form):
       return super().form_valid(form)


class PostUpdateView(UpdateView):
   form_class = PostForm
   template_name = 'post/update.html'
   success_url = reverse_lazy('post:index')


   def form_valid(self, form):
       return super().form_valid(form)


   def get_queryset(self):
       return Post.objects.all()


class PostDeleteView(DeleteView):
   model = Post
   success_url = reverse_lazy('post:index')
   template_name = 'post/delete.html'


   def get_object(self, queryset=None):
     post_id = self.request.POST.get('pk')
     return self.get_queryset().filter(pk=post_id).get()


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
            post_conteudo = form.cleaned_data['conteudo']
            post_data_postagem = form.cleaned_data['data_postagem']
            post_poster_url = form.cleaned_data['poster_url']
            post = Post(name=post_name,
                          release_year=post_release_year, conteudo = post_conteudo,
                          data_postagem = post_data_postagem, poster_url=post_poster_url)
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
            post_conteudo = form.cleaned_data['conteudo']
            post_data_postagem = form.cleaned_data['data_postagem']
            post.poster_url = form.cleaned_data['poster_url']
            post.save()
            return HttpResponseRedirect(
                reverse('post:detail', args=(post.id, )))
    else:
        form = PostForm(
            initial={
                'name': post.name,
                'release_year': post.release_year,
                'conteudo' : post.conteudo,
                'data_postagem' : post.data_postagem,
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
    
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment_data_postagem= form.cleaned_data['data_postagem']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            data_postagem=comment_data_postagem,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('post:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'post/comment.html', context)

