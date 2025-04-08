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

 @receiver(post_delete, sender=FileArchivo)
 def eliminar_archivo(sender, instance, **kwargs):
    if instance.archivo:
        instance.archivo.delete(False)


@receiver(pre_save, sender=FileArchivo)
def actualizar_archivo(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance =  FileArchivo.objects.get(pk=instance.pk)
        if  old_instance.archivo and   old_instance.archivo != instance.archivo:
            old_instance.archivo.delete(save=False)

    except FileArchivo.DoesNotExist:
        pass        
    
        
     
        

