from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path("", views.index, name= 'index'),
    path('post/', views.post, name= 'post'),
    path('<int:post_id>/', views.detail, name= 'detail'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact , name='contact')
]