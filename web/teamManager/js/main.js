//Api de PokemonApi
let basePokeApi = 'https://pokeapi.co/api/v2/';

//Data del usuario
let data = {};

/**
 * Creará la estructura HTML de una card para mostrar la información de un pokemon
 * Toma en cuenta si el pokemon forma parte de los FAVS o TEAM del usuario
 * @param {object} pokemon Contiene la información a mostrar
 */
const createPokemonCard = (pokemon) => {
    //Construcción del div de las cartas
    //Se crea así para poder manipular su  contenido, de otra forma no funciona
     let wrapper = document.createElement('div');
     //Añado las clases que tiene el contenedor
     wrapper.classList.add('col','mb-4');
     //Valores por defecto
     const favColor = 'text-secondary';
     const teamColor = 'text-secondary'
     const cardImg = pokemon.img || "./img/default_pokebola.png"; 
     //Contenido de la card
     const cardContent = `<div class="card">
     <img src="${cardImg}" class="card-img-top" alt="${pokemon.name}">
     <div class="card-body">
         <h5 class="card-title">${pokemon.name}</h5>
         <p class="card-text">${pokemon.description}</p>
     </div>
     <div class="card-footer d-flex">
         <button type="button" class="btn btn-light"><i
                 class="fas fa-heart ${favColor}"></i></button>
         <button type="button" class="btn btn-light ml-auto"><i
                 class="fas fa-bookmark ${teamColor}"></i></button>
     </div>
 </div>`;
 //Agregando todo el HTML en el contenido del wrapper
 wrapper.innerHTML = cardContent; 
 return wrapper;
}

/**
 * Muestra la lista de Cards en elemento especificado
 * Reemplazará el contenido actual por el de la lista
 * @param {array pokemon} list 
 * @param {DOMElemento} target 
 */
const showListAsCard = (list,target) => {
    list.forEach(pokemon => {
        //Agregando (haciendo hijo) el pokemon al lugar donde lo queremos para que pertenezca ahí
        target.appendChild(createPokemonCard(pokemon));
    });
}

/**
 * Configura todo lo necesario para que la App funcione
 */
const App = () => {
    console.log('Start App');
    const pokemons = Array(4)
    .fill({})
    .map((element, index) => {
        return{
            name: `Pokemon ${index}`, 
            img: "./img/default_pokebola.png",
            description: "Lorem ipsum dolor sit amet consectetur"
        };
    });
    showListAsCard(pokemons, document.querySelector('.discover-result'));
};

//Cuando la ventana se cargue, no importa donde se ponga el script, funcionará
window.onload = App;