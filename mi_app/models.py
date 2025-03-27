from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='fotos/')
    video = models.FileField(upload_to='videos/')
    archivo = models.FileField(upload_to='archivos/')

    def __str__(self):
        return self.nombre



class Gif(models.Model):
    nombre = models.CharField(max_length=255, help_text="Nombre identificador del GIF")
    imagen = models.ImageField(upload_to='gifs/', help_text="Archivo GIF")
    activo = models.BooleanField(default=True, help_text="Indica si el GIF se usa actualmente en los estilos")

    def __str__(self):
        return self.nombre

