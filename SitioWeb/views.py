from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import profesorForm

class CustomLoginView(LoginView):
    template_name = 'templates/Modals.html'
    
    
# Create your views here.
def index(request):
    context={}
    return render(request,'paginas/index.html',context)

def Contacto(request):
    context={}
    return render(request,'paginas/Contacto.html', context)

def agregarProfesor(request):

    data = {
        'form': profesorForm()
    }

    if request.method == 'POST':
        formulario = profesorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Profesor Guardado Correctamente"
        else:
            data["mensaje"] = formulario

    return render(request,'paginas/agregarProfesor.html', data)









def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirigir a una página de éxito.
            return redirect('nombre_de_tu_url_después_del_login')
        else:
            # Retornar un mensaje de error de 'login' inválido.
            return render(request, 'tu_template_de_login.html', {'error': 'Usuario o contraseña inválidos.'})
    else:
        return render(request, 'tu_template_de_login.html')
