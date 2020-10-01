//Variables
let exit = false;
let array = [];

//Objeto
let Objeto = {events:array}

//Funcion
function eventOptions(ev,x){
    if(x==false)
        Objeto.events = array.push(ev);
    else Objeto.events = array.pop();
};
//
do{
    console.log("Qué desea hacer?");
    console.log("1) Agregar evento");
    console.log("2) Quitar eventos");
    console.log("3) Ver eventos");
    console.log("4) Salir");

    let p = prompt("Elija su opción");
    switch(p){
        case "1": 
            let ev = prompt("Ingrese un evento");
            eventOptions(ev,false);
        break;

        case "2":
            eventOptions(array, true);
        break;

        case "3":
             console.log(array);
        break;

        case "4":
            console.log("Saliendo...");
             exit=true;
        break;

        default: console.log("Opción errónea");
        break;
    }

}while(exit==true);
