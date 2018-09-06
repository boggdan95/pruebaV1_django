var socket = io('http://localhost:5000');

var description_decode;
var numero;

function startTraining() {
  numero = 0;
  document.getElementById("button_start").style.display = "none";
  var description = document.getElementById("hide_description").textContent;
  description_decode = JSON.parse(description);
  tiempo = description_decode.time;
  secuencial = description_decode.is_secuencial;
  reps = description_decode.reps;
  modules = description_decode.modules;
  tipo = description_decode.typeReaction;
  console.log(tiempo, secuencial, reps, modules, tipo);
  temporizador(tiempo);
  socket.emit('entrenamiento general', tipo,tiempo,reps,modules,is_secuencial);
}

  socket.on('results', function(tiempo,mensaje){
    introduceResults(tiempo,message);
    numero = numero + 1;
  });

//Insertar resultados
function introduceResults(tiempo,message) {
  var table = document.getElementById("results_table");
  var row = table.insertRow(-1);
  var cell1 = row.insertCell(0);
  var cell2 = row.insertCell(1);
  var cell3 = row.insertCell(2);
  cell1.innerHTML = numero;
  cell2.innerHTML = tiempo;
  cell3.innerHTML = message;
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


function temporizador(time){
  var tiempo = time;
  var x = setInterval(function(){

    minutes = (tiempo / 60) | 0;
    seconds = (tiempo % 60) | 0;
    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;
    document.getElementById("timer").innerHTML = minutes +" : " + seconds;
    tiempo--;

    if(seconds == 00 && minutes > 0){
      minutes--;
      seconds = 60;
      if (minutes == 0){
         minutes = 0;
      }
    }
    if (seconds <= 00 && minutes <= 0) {
      clearInterval(x);
      document.getElementById("timer").innerHTML = "Entrenamiento finalizado";
      document.getElementById("btn_home").style.display = "block";
      document.getElementById("btn_results").style.display = "block";
    }

  },1000);
}