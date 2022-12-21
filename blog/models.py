from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from .utils import set_slug

from tinymce import models as tinymce_models


class Posteo(models.Model):
    titulo = models.CharField(max_length= 200, null= True)
    slug = models.SlugField(max_length= 200, null= False, blank= True, editable= False)
    # autor = models.ForeignKey(Usuario, on_delete= models.CASCADE, related_name= 'blog_posts')
    copete = models.CharField(max_length= 200, null= True)
    # contenido = models.TextField(null= True)
    contenido = tinymce_models.HTMLField(null= True)
    imagen_encabezado = models.ImageField(upload_to= 'images/', null= True, blank= True)
    creacion = models.DateTimeField(auto_now_add= True)
    modificacion = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-creacion']    # Para ordenar los post por su fecha de creacion en las querys

    def __str__(self):
        return self.titulo

# Genera un url en forma automatica
pre_save.connect(set_slug, sender= Posteo)