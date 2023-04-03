from django.shortcuts import render
from math import pi

# Create your views here.

def Atividade2(request):
    if request.method == 'GET':
        return render(request, "base2.html")
    elif request.method == 'POST':
        h = float(request.POST.get('h'))
        r = float(request.POST.get('r'))
        Volume = ((pi * r**2 + h)/2)
    print (Volume)
    
    return render(request, "base2.html")

