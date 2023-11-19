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

