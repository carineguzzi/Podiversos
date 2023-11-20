from django.db import models
from django.conf import settings


class Post(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    conteudo = models.CharField(max_length=400)
    data_postagem = models.DateTimeField()
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name} ({self.release_year})'

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    data_postagem = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

    class Meta:
       ordering = ('-data_postagem',)
