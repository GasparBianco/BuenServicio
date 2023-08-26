from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'autentificacion/login.html')

def checkLogout(request):
    return render(request, 'auth/checklogout.html')