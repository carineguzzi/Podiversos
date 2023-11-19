from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'name',
            'release_year',
            'conteudo',
            'data_postagem',
            'poster_url',
        ]
        labels = {
            'name': 'Título',
            'release_year': 'Data de Lançamento',
            'conteudo': 'Conteudo da Postagem',
            'data_postagem': 'Data da Postagem',
            'poster_url': 'URL do Poster',
        }