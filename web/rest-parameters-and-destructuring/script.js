//Rest Numbers
/*
Al poner los tres puntos, puedo recibir muchos parámetros
*/
function min(...numbers){
    let result = Infinity;
    for(let number of numbers){
        if(number < numbers) result=number;
    }
    return result;
};

//>_ min(1,2,3,4,-1,23,100)
//>_ -1


// También puede sobreescribir
let array = [1,2,3];
// console.log([-1,0, ...array]);
// [-1,0,1,2,3]

//Destructuring
/*
- Desconstruye un arreglo y le da valores de referencia por ejemplo
- Puede hacerse con objetos, arreglos...
*/


let arr = [1,2,3,4];
let [a,b,c,d] = arr;
//a=1, b=2, c=3, d=4
