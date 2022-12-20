from django.urls import path
from . import views

# app_name = 'blog'

urlpatterns = [
    path("", views.index, name= 'index'),
    path('<slug:slug_text>/', views.post, name= 'post'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact , name='contact')
]