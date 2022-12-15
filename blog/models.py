from django.db import models

class Posteo(models.Model):
    titulo = models.CharField(max_length= 200, unique= True)
    # slugField
    # usuario = 
    contenido = models.TextField()
    # imagen = 
    creacion = models.DateTimeField(auto_now_add= True)
    modificacion = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-creacion']    # Para ordenar los post por su fecha de creacion en las querys
    
    def __str__(self):
        return self.titulo