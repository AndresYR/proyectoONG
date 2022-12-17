from django.db import models

class Posteo(models.Model):
    titulo = models.CharField(max_length= 200, unique= True)
    # slug = models.SlugField(max_length=200, unique= True)
    # autor = models.ForeignKey(Usuario, on_delete= models.CASCADE, related_name= 'blog_posts')
    descripcion = models.CharField(max_length=400, null= True)
    contenido = models.TextField(null= True)
    # imagen = 
    creacion = models.DateTimeField(auto_now_add= True)
    modificacion = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-creacion']    # Para ordenar los post por su fecha de creacion en las querys
    
    def __str__(self):
        return self.titulo