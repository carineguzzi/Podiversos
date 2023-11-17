from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'release_year',
            'poster_url',
        ]
        labels = {
            'name': 'Título',
            'release_year': 'Data de Lançamento',
            'poster_url': 'URL do Poster',
        }