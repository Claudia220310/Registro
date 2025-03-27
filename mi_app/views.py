from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario, Gif  # Asegúrate de tener el modelo Gif definido

def registro(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')  # Redirecciona a la vista de éxito
    else:
        form = UsuarioForm()
    
    # Consulta el GIF activo para usarlo como fondo
    gif = Gif.objects.filter(activo=True).first()
    
    return render(request, 'formulario.html', {'form': form, 'gif': gif})

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')

def info_view(request):
    usuarios = Usuario.objects.all()  # Obtiene todos los usuarios registrados
    return render(request, 'info.html', {'usuarios': usuarios})
