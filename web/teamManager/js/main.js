//Api de PokemonApi
let basePokeApi = 'https://pokeapi.co/api/v2/';

//Data del usuario
let data = {
    //Número aleatorio desde 1 hasta 1050
    offset: Math.floor(Math.random()*1050) + 1,
    limit: 4,
};

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
 * Obtiene una lista de pokemons a mostrar
 * @param {function} action callback cuando la función termine de obtener los datos 
 */
const getDiscoverPokemon = (action) => {
    const endPoint = basePokeApi+`pokemon?limit=${data.limit}&offset=${data.offset}`;
    fetch(endPoint)
    .then(response => response.json())
    .then(data => {
        action(data);
    })
    .catch(error => {
        console.log('Error obtenido de la lista de Pokemons para discover',error);
    });
}

/**
 * Dada la data de un pokemon la mapea a un objeto pokemon más simple
 * @param {object} Data data de un pokemon en formato API
 */
const createPokemon = (data) => {
    return{
        name: data.species.name.toUpperCase(),
        img: data.sprites.front_default,
        description: "This pokemon has the types: " +
        data.types.reduce((typesText,current) => {
            return (typesText == "" ? "" : typesText + ",") + current.type.name;
        },""),
    }
}

/**
 * Muestra la sección Discover como una lista de cartas
 * Obtiene los elementos a mostrar desde data.discover
 */
const showDiscover = async () => {
    let pokemons = [];
    for (const pokemonMetaData of data.discover.results){
        const response = await fetch(pokemonMetaData.url);
        const data = await response.json();
        let pokemon = createPokemon(data);
        pokemons.push(pokemon);
    };
    showListAsCard(pokemons, document.querySelector('.discover-result'));
}

/**
 * Configura todo lo necesario para que la App funcione
 */
const App = () => {
    console.log('Start App');
    //Obteniendo la data discover
    getDiscoverPokemon(discover => {
        data.discover = discover;
        showDiscover();
    });
    // showListAsCard(pokemons, document.querySelector('.discover-result'));
};

//Cuando la ventana se cargue, no importa donde se ponga el script, funcionará
window.onload = App;