from django.shortcuts import render
from.models import Inmueble

# Create your views here.
def lista_inmuebles(request):
    inmuebles = Inmueble.objects.all()#Sleccionar*from portal_imueble
    #print(inmuebles)
    context = {
        'inmuebles':inmuebles
    }
    return render(request,'portal/index.html', context)
