from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'templates/Modals.html'
    
    
# Create your views here.
def index(request):
    context={}
    return render(request,'paginas/index.html',context)

def Contacto(request):
    context={}
    return render(request,'paginas/Contacto.html', context)