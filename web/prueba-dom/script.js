function hello(){
    console.log('hello');
}

var motivate = function(){
    console.log('juuuuust doooo iiiiit xd');
}

var saludar = (nombre = "Nestor") =>{
    console.log(`Hola ${nombre}, que guapo andas`);
}

//Callback
var pass = (x) =>{
    console.log("Obteniendo datos de internet...");
    x();
    console.log("Terminado prro");
}