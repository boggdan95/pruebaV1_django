var socket = io();

socket.emit("trainning","Ready");

//Timer function
window.onload = function(){
   var tiempo = 5;
   var x = setInterval(function(){

     minutes = (tiempo / 60) | 0;
     seconds = (tiempo % 60) | 0;

     console.log(minutes);
     console.log(seconds);

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
       //Creacion de boton de retorno cuando el entreno ha finalizado
       myButton = document.createElement("input");
       myButton.type = "button";
       myButton.value = "Regresar"; //texto del boton
       myButton.className = "btn_return"; //clase de estilo del boton
       myButton.onclick = function () {history.back();}; //funcion del boton
       document.getElementById("backPanel").appendChild(myButton); //agregado al panel
     }

   },1000);
 }
