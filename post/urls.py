from django.urls import path

from . import views

app_name = 'post'
urlpatterns = [
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('', views.PostListView.as_view(), name='index'),
    path('update/<int:post_id>/', views.update_post, name='update'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
]