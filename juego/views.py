from django.shortcuts import render
from .models import Pregunta, Respuesta
# Create your views here.
def listar_preguntas(request):
    data = {}
    preguntas = Pregunta.objects.all().order_by('?')[:3]
    for item in preguntas:
        respuestas = Respuesta.objects.filter(id_pregunta=item.id)
        data[item.pregunta]= respuestas

    return render(request, 'juego/listar_preguntas.html', {"preguntas":data})
