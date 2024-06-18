from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    context={}
    return render(request,'paginas/index.html',context)

def Contacto(request):
    context={}
    return render(request,'paginas/Contacto.html', context)




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

def crud(request):
    consulta = consulta.objects.all()
    context = {'consulta':consulta}
    return render(request, 'SitioWeb/listaConsulta.html',context)

def consultasAdd(request):
    if request.method is not "POST":
        nombre = nombre.objects.all()
        context = {'nombre':nombre}
        return render(request, 'automovil/autos_add.html',context)
    else:
        
        id_consulta = request.POST["idConsulta"]
        nombre_c = request.POST["Nombre"]
        apellido_c = request.POST["Apellido"]
        numero_c = request.POST["Numero"]
        correo_c = request.POST["Correo"]
        
        objetoNombre = nombre.objects.all(id_nombre = nombre)
        objetoConsulta = id_consulta.objects.create(
            id_consulta = id_consulta,
            id_nombre = objetoNombre,
            apellido_c = apellido_c,
            numero_c = numero_c,
            correo_c = correo_c,
            
        )
        objetoNombre.save()
        context = {'mensaje':'OK, datos guardados...'}
        return render(request, 'SitioWeb/añadirConsulta.html',context)
    
    return render(request, 'tu_template_de_login.html', {'login_success': True})

    return render(request, 'tu_template_de_login.html', {'login_success': False, 'error_message': 'Usuario o contraseña inválidos.'})
