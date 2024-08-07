from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import profesorForm, Profesor, consultaForm, Consulta, EstadoForm
from .models import Profesor, Consulta
from django.contrib.auth.decorators import permission_required

class CustomLoginView(LoginView):
    template_name = 'templates/Modals.html'
    
    
# Create your views here.
def index(request):
    context={}
    return render(request,'paginas/index.html',context)

def Contacto(request):
    data = {
        'form': consultaForm()
    }

    if request.method == 'POST':
        formulario = consultaForm(data=request.POST)
        if formulario.is_valid():
            consulta = formulario.save(commit=False)
            if not formulario.cleaned_data['curso']:
                consulta.curso = None
            consulta.save()
            return render(request, 'paginas/Contacto.html', {'form': consultaForm(), 'mensaje': "Consulta Enviada Correctamente"})
        else:
            data["mensaje"] = formulario.errors

    return render(request, 'paginas/Contacto.html', data)

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

@permission_required('SitioWeb.view_consulta')
def listarConsulta(request):
    listarConsulta = Consulta.objects.all()
    return render(request, 'paginas/listarConsulta.html', {'Consulta': listarConsulta})

def modificarProfesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    data = {
        'form': profesorForm(instance=profesor),
        'profesor': profesor
    }
    if request.method == 'POST':
        formulario = profesorForm(data=request.POST, instance=profesor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarProfesor')
        else:
            data['form'] = formulario
    return render(request, 'paginas/modificarProfesor.html', data)

def eliminarProfesor(request, id):
    profesor = get_object_or_404(Profesor, id=id)
    profesor.delete()
    return redirect('listarProfesor')

def eliminarConsulta(request, id):
    consulta = get_object_or_404(Consulta, id_consulta=id)
    consulta.delete()
    return redirect('listarConsulta')

def estadoConsulta(request, id):
    consulta = get_object_or_404(Consulta, id_consulta=id)
    
    if request.method == 'POST':
        estado_form = EstadoForm(request.POST, instance=consulta)
        if estado_form.is_valid():
            estado_form.save()
            return redirect('listarConsulta') 
    else:
        estado_form = EstadoForm(instance=consulta)
    
    data = {
        'consulta': consulta,
        'estado_form': estado_form,
    }
    return render(request, 'paginas/estadoConsulta.html', data)






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


def menu(request):
    request.session["usuario"]="utp"
    usuario = request.session["usuario"]
    context = {'usuario':usuario}
    return render(request,'administrador/menu.html')