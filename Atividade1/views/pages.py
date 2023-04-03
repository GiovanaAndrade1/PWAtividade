import logging
from email.errors import MessageError
from django.shortcuts import render
from django.contrib import messages

def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    elif request.method == "POST":
        DNA = request.POST.get('DNA')
        print(DNA)
        a = 0
        g = 0
        c = 0
        t = 0
        string = ""
        Error = ""

        for i in DNA:
            if i == "A":
                a = a + 1
                string += "T"
            elif i == "G":
                g = g + 1
                string += "C"
            elif i == "C":
                c = c + 1
                string += "G"
            elif i == "T":
                t = t + 1
                string += "A"
            else:
                Error = "Erro, Base nitrogenada incorreta"
                break

        try:
            terminal = {
                'num_adenina': f"A:{a}",
                'num_guanina': f"G:{g}",
                'num_citosina': f"C:{c}",
                'num_timina': f"T:{t}",
                'nova_string': f"Fita complementar: {string}",
                'Error': Error
            }
        except MessageError as e:
            messages.error(request, "Base incorreta")
        else:
            messages.success(request, "Tudo certo")

            
        
        return render(request, "home.html", context=terminal)
    

   