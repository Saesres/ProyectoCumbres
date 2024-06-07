console.log("js cargado")
function limpiar_campos() { 
document.getElementById("nombre").value = '';
document.getElementById("apellido").value ='';
document.getElementById("telefono").value = '';
document.getElementById("correo").value = '';
document.getElementById("consulta").value = '';
}


function stopVideo() {
  const myVideo = document.getElementById("myVideo");
  myVideo.pause();
  myVideo.currentTime = 0;
  const videoPlayer = document.getElementById("videoPlayer");
  videoPlayer.style.display = "none";
}
function playVideo(file) {
  const myVideo = document.getElementById("myVideo");
  myVideo.src = file;
  const videoPlayer = document.getElementById("videoPlayer");
  videoPlayer.style.display = "block";
  myVideo.autoplay = true;
}
function validarInicioSesion() {
  const usuario = document.getElementById('miTextboxNUsuario').value;
  const contraseña = document.getElementById('TextboxContraseña').value;

  if (usuario.trim() === '') {
      alert('ingresa tu nombre de usuario.');
      return false;
  }
  if (contraseña.trim() === '') {
      alert('ingresa tu contraseña.');
      return false;
  }

  const usuarioEnMayusculas = usuario.toUpperCase();

  // USUARIO = ADMIN
  // CLAVE = PassCumbres2024

  if (usuarioEnMayusculas === 'ADMIN' && contraseña === 'PassCumbres2024') {
      alert('Inicio de sesión exitoso. ¡Bienvenido, ' + usuario + '!');
      return true;
  } else {
      alert('Usuario o contraseña incorrecta');
      return false;
  }
}

function validarConsulta() {
  const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const telefono = document.getElementById('telefono').value;
    const correo = document.getElementById('correo').value;
    const consulta = document.getElementById('consulta').value;

    if (nombre.trim() === '') {
        alert('El campo nombre es obligatorio');
        return false;
    }
    if (apellido.trim() === '') {
        alert('El campo apellido es obligatorio');
        return false;
    }
    if (telefono.trim() === '') {
      alert('El campo teléfono es obligatorio');
      return false;
  } else {
      if (telefono.trim().length !== 9) {
          alert('El teléfono debe tener 9 dígitos');
          return false;
      }
      const telefonoRegex = /^[0-9]+$/;
      if (!telefonoRegex.test(telefono.trim())) {
          alert('El campo teléfono debe contener solo números');
          return false;
      }
  }
  if (correo.trim() === '') {
    alert('El campo correo es obligatorio');
    return false;
} else {
    const correoRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!correoRegex.test(correo.trim())) {
        alert('Ingresa una dirección de correo electrónico válida');
        return false;
    }
}
    if (consulta.trim() === '') {
      alert('Ingresa una consulta');
      return false;

    }
    alert('Consulta enviada con exito,nos contactaremos con usted a la brevedad');
}

