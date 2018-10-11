from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

def post_list(request):
    publicaciones = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/post_list.html', {'publicaciones': publicaciones})
