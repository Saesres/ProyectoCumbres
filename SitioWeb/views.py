from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import profesorForm, Profesor
from .models import Profesor

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

def listarProfesor(request):
    listarProfesor = Profesor.objects.all()
    return render(request, 'paginas/listarProfesor.html', {'Profesor': listarProfesor})

def modificarProfesor(request, id):

    profesor = get_object_or_404(Profesor, id=id)

    data = {
        'form': profesorForm(instance=profesor)
    }

    if request.method == 'POST':
        formulario = profesorForm(data=request.POST, instance=profesor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listarProfesor")
    
    return render(request,'paginas/modificarProfesor.html', data)




def eliminarProfesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    profesor.delete()
    return redirect('listarProfesor')







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
