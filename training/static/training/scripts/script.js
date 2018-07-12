var socket = io();

var nombre, apellido, edad, tipoEntrenamiento, tiempoEntrenamiento, modulosEntrenamiento, moduloColor;

function athlete(nombre,apellido,edad){
  this.nombre = nombre;
  this.apellido  = apellido;
  this.edad = edad;
}


function randomInt (low, high) {
    return Math.floor(Math.random() * (high - low + 1) + low);
}

function startTrainning() {
  typeOfTrainning();
  var entrenamiento = { "Reaccion":tipoEntrenamiento, "Tiempo":tiempoEntrenamiento, "Modulo":modulosEntrenamiento};
  var myJSON = JSON.stringify(entrenamiento);
  socket.emit("designTrainnig",myJSON);
}


//Entrenamiento seleccionado
function typeOfTrainning(){
  var tipo = document.getElementById("reaccion");
  var tiempo = document.getElementById('tiempo');
  var modulos = document.getElementById('modulo');

  tipoEntrenamiento = tipo[tipo.selectedIndex].text;
  tiempoEntrenamiento = tiempo[tiempo.selectedIndex].text;
  modulosEntrenamiento = modulos[modulos.selectedIndex].text;

  console.log(tipoEntrenamiento);
  console.log(tiempoEntrenamiento);
  console.log(modulosEntrenamiento);

}

//Verificar campos de entrada del usuario
function fillForm() {
    var message = document.getElementById("message");
    nombre = document.getElementById("name").value;
    apellido = document.getElementById('lastName').value;
    edad = document.getElementById('age').value;
    var error_fill = 0;
    message.innerHTML = "";

    try {
        if(nombre === "" || apellido === "")  throw "sus datos, por favor";
        if(typeof nombre !== "string" || typeof apellido !== "string")  throw "su nombre y apellido";
        if(edad <= 0)    throw "una edad válida";
    }
    catch(err) {
        message.innerHTML = "Ingrese " + err;
        error_fill = 1;
    }
    finally {
        document.getElementById("name").value = "";
        document.getElementById("lastName").value = "";
        document.getElementById("age").value = "";
    }
    //envio datos al servidor
    if(error_fill === 0){
      //sendToServer();
      message.innerHTML = "Se ha enviado su información exitosamente"
    }


}

//Instrucciones dependiendo el juego seleccionado
function selectGame(value){
  var contenido = document.getElementById('content');
  if (value === 1){
    console.log("Boton 1");
    contenido.innerHTML = "<p class=instruccion>Este juego consiste en un tipo de entrenamiento sencillo, donde solo utilizaremos un módulo. El módulo se encenderá de un <strong>único color</strong> y en cuanto encienda, usted debe reaccionar para desactivarlo. Esto sucederá dentro de un intervalo de <strong>1 minuto y medio</strong>, la  cantidad de veces que se encenderá el módulo variará entre <strong>10 a 25</strong> repeticiones. El tiempo a medir es el que transcurre desde que se activo la luz hasta desactivarla mediante un toque. Si tarda más de 3 segundos en módulo se desactivará automaticamente y esperará hasta su siguiente activación para ser apagado por el atleta.</p><a href=games.html><button class=btn_return>Regresar</button></a><a href=resultadosEntrenamiento.html><button class=button_game onclick=game(1)>Continuar</button></a>";
  }
  else if (value === 2){
    console.log("Boton 2");
    contenido.innerHTML = "<p class=text2>Instrucciones 2</p><a href=games.html><button class=btn_return>Regresar</button></a><a href=resultadosEntrenamiento.html><button class=button_game>Continuar</button></a>";

  }
  else if (value === 3){
    console.log("Boton 3");
    contenido.innerHTML = "<p class=text2>Instrucciones 3</p><a href=games.html><button class=btn_return>Regresar</button></a><a href=resultadosEntrenamiento.html><button class=button_game>Continuar</button></a>";
  }
}


//Generar valores para los entrenamientos preprogramados
function game(value){
  if (value === 1){
    console.log("Juego 1");
    socket.emit('entrenamiento1',randomInt(10,25));
  }
}

//Obtener el color seleccionado para los módulos
function colorSelect() {
  if (document.getElementById("rdbtn1").checked) {
    moduloColor = "blue";
  }
  if (document.getElementById("rdbtn2").checked) {
    moduloColor = "red";
  }
  if (document.getElementById("rdbtn3").checked

) {
    moduloColor = "green";
  }

  console.log(moduloColor);
}
