from django.urls import path
from .views import registro, registro_exitoso, info_view

urlpatterns = [
    path('', registro, name='registro'),
    path('registro_exitoso/', registro_exitoso, name='registro_exitoso'),
    path('info/', info_view, name='info'),
]
