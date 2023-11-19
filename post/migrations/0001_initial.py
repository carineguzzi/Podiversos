# Generated by Django 4.2.7 on 2023-11-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('conteudo', models.CharField(max_length=400)),
                ('data_postagem', models.DateTimeField()),
                ('poster_url', models.URLField(null=True)),
            ],
        ),
    ]
