from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name= 'index'),
    path('post/<slug:slug_text>/', views.detail, name= 'detail'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact , name='contact'),
    path('photos/', views.photos , name='photos'),
]