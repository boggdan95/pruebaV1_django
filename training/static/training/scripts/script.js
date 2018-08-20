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
  if (document.getElementById("rdbtn3").checked) {
    moduloColor = "green";
  }
  console.log(moduloColor);
}
