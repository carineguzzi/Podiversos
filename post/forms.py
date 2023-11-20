from django.forms import ModelForm
from .models import Post, Comment


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
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
            'data_postagem'
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
            'data_postagem':'Data'
        }
