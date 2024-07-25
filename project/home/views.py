from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Asegúrate de que el nombre del archivo es correcto y que está en el lugar correcto
