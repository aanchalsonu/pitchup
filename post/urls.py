from django.urls import path
from . import views

app_name = 'post'


urlpatterns = [
    path('', views.Index, name='index'),
    path('newpost/', views.NewPost, name='newpost'),
    path('<uuid:post_id>', views.PostDetails, name="postdetails"),
    path('<uuid:post_id>/like', views.like, name='postlike'),
    path('delete/<uuid:post_id>/', views.delete_post, name='delete_post'),
]
