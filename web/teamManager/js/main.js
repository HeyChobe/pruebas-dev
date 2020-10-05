//Api de PokemonApi
let basePokeApi = "https://pokeapi.co/api/v2/";

//Data del usuario
let data = {};
let searchResult = [];

const saveData = () => {
  //Creando par key-value en LocalStorage
  localStorage.setItem("data", JSON.stringify(data));
};

/**
 * Creará la estructura HTML de una card para mostrar la información de un pokemon
 * Toma en cuenta si el pokemon forma parte de los FAVS o TEAM del usuario
 * @param {object} pokemon Contiene la información a mostrar
 */
const createPokemonCard = (pokemon) => {
  //Construcción del div de las cartas
  //Se crea así para poder manipular su  contenido, de otra forma no funciona
  let wrapper = document.createElement("div");
  //Añado las clases que tiene el contenedor
  wrapper.classList.add("col", "mb-4");
  //Valores por defecto
  const favColor =
    data.favs.findIndex((favPokemon) => pokemon.name == favPokemon.name) >= 0
      ? "text-danger"
      : "text-secondary";
  const teamColor =
    data.team.findIndex((teamPokemon) => pokemon.name == teamPokemon.name) >= 0
      ? "text-primary"
      : "text-secondary";
  const cardImg = pokemon.img || "./img/default_pokebola.png";
  //Contenido de la card
  const cardContent = `<div class="card">
     <img src="${cardImg}" class="card-img-top" alt="${pokemon.name}">
     <div class="card-body">
         <h5 class="card-title">${pokemon.name}</h5>
         <p class="card-text">${pokemon.description}</p>
     </div>
     <div class="card-footer d-flex">
         <button data-pokemon='${JSON.stringify(
           pokemon
         )}' type="button" class="btn btn-light fav-pokemon ${pokemon.name}">
         <i class="fas fa-heart ${favColor}"></i>
         </button>
         <button data-pokemon='${JSON.stringify(
           pokemon
         )}' type="button" class="btn btn-light ml-auto team-pokemon ${
    pokemon.name
  }">
         <i class="fas fa-bookmark ${teamColor}"></i>
         </button>
     </div>
 </div>`;
  //Agregando todo el HTML en el contenido del wrapper
  wrapper.innerHTML = cardContent;
  return wrapper;
};

/**
 * Muestra la lista de Cards en elemento especificado
 * Reemplazará el contenido actual por el de la lista
 * @param {array pokemon} list
 * @param {DOMElemento} target
 */
const showListAsCard = (list, target) => {
  target.innerHTML = "";
  list.forEach((pokemon) => {
    //Agregando (haciendo hijo) el pokemon al lugar donde lo queremos para que pertenezca ahí
    target.appendChild(createPokemonCard(pokemon));
  });
};

/**
 * Obtiene una lista de pokemons a mostrar
 * @param {string} endPoint
 * @param {function} action callback cuando la función termine de obtener los datos
 */
const getDiscoverPokemon = (endPoint, action) => {
  fetch(endPoint)
    .then((response) => response.json())
    .then((data) => {
      action(data);
    })
    .catch((error) => {
      console.log(
        "Error obtenido de la lista de Pokemons para discover",
        error
      );
    });
};

/**
 * Dada la data de un pokemon la mapea a un objeto pokemon más simple
 * @param {object} Data data de un pokemon en formato API
 */
const createPokemon = (data) => {
  return {
    name: data.species.name.toUpperCase(),
    img: data.sprites.front_default,
    description:
      "This pokemon has the types: " +
      data.types.reduce((typesText, current) => {
        return (typesText == "" ? "" : typesText + ",") + current.type.name;
      }, ""),
  };
};

/**
 * Muestra la sección Discover como una lista de cartas
 * Obtiene los elementos a mostrar desde data.discover
 */
const showDiscover = async () => {
  let pokemons = [];
  for (const pokemonMetaData of data.discover.results) {
    const response = await fetch(pokemonMetaData.url);
    const data = await response.json();
    let pokemon = createPokemon(data);
    pokemons.push(pokemon);
  }
  showListAsCard(pokemons, document.querySelector(".discover-result"));
};

/**
 * Almacena el resultado de búsqueda de pokemón
 * @param {object} discover
 */
const saveDiscoverData = (discover) => {
  data.discover = discover;
  showDiscover();
};

/**
 * Obtiene los pokemons siguientes la los mostrados
 */
const nextDiscoverListener = () => {
  document.querySelector(".discover-next").addEventListener("click", (e) => {
    e.preventDefault(); //Evita el comportamiento por defecto
    getDiscoverPokemon(data.discover.next, saveDiscoverData);
  });
};

/**
 * Obtiene los pokemons anteriores la los mostrados
 */
const previousDiscoverListener = () => {
  document
    .querySelector(".discover-previous")
    .addEventListener("click", (e) => {
      e.preventDefault(); //Evita el comportamiento por defecto
      getDiscoverPokemon(data.discover.previous, saveDiscoverData);
    });
};

const listToggle = (target, list, after) => {
  const pokemonToAddOrRemove = JSON.parse(target.dataset.pokemon);
  const index = list.findIndex(
    (pokemon) => pokemon.name == pokemonToAddOrRemove.name
  );
  //Está en la lista
  if (index >= 0) list.splice(index, 1);
  //Desde el index elimina uno
  else {
    list.push(pokemonToAddOrRemove);
  }
  //Guardando la data en LocalStorage
  saveData();
  if (after) after(pokemonToAddOrRemove);
};

const favListener = () => {
  document.addEventListener("click", (e) => {
    //Delegación de un evento
    let target = e.target; //Cuando se clickea el elemento
    if (
      target.classList.contains("fav-pokemon") ||
      target.parentElement.classList.contains("fav-pokemon")
    ) {
      target = target.dataset.pokemon ? target : target.parentElement;
      listToggle(target, data.favs, (pokemon) => {
        document
          .querySelectorAll(".fav-pokemon." + pokemon.name)
          .forEach((favs) => {
            const i = favs.querySelector("i");
            i.classList.toggle("text-danger");
            i.classList.toggle("text-secondary");
          });
        showListAsCard(data.favs, document.querySelector(".favs-result"));
      });
    }
  });
};

const teamListener = () => {
  document.addEventListener("click", (e) => {
    //Delegación de un evento
    let target = e.target; //Cuando se clickea el elemento
    if (
      target.classList.contains("team-pokemon") ||
      target.parentElement.classList.contains("team-pokemon")
    ) {
      target = target.dataset.pokemon ? target : target.parentElement;
      listToggle(target, data.team, (pokemon) => {
        document
          .querySelectorAll(".team-pokemon." + pokemon.name)
          .forEach((team) => {
            const i = team.querySelector("i");
            i.classList.toggle("text-primary");
            i.classList.toggle("text-secondary");
          });
        showListAsCard(data.team, document.querySelector(".team-result"));
      });
    }
  });
};

const searchListener = () => {
    let searchPanel = document.querySelector("#search");
    document.forms.search.addEventListener('submit', e => {
        e.preventDefault();
        let value=document.forms.search.querySelector("input").value;
        fetch(basePokeApi+"pokemon/"+value)
        .then(response => response.json())
        .then(data => {
            searchPanel.classList.remove("d-none");
            let pokemon = createPokemon(data);
            if((searchResult.findIndex(p => pokemon.name == p.name))<0){
                searchResult.push(pokemon);
            }

            showListAsCard(searchResult, document.querySelector(".search-result"));
        })
        .catch(error => {
            console.log("No se obtuvo el pokemon");
        })
    });

    searchPanel.querySelector(".close-search").addEventListener('click', e => {
        searchPanel.classList.add("d-none");
        searchResult = [];
    });
}

/**
 * Añade las llamadas de los eventos dentro de la ventana en funcionamiento
 */
const addListeners = () => {
  nextDiscoverListener();
  previousDiscoverListener();
  favListener();
  teamListener();
  searchListener();
};

/**
 * Configura todo lo necesario para que la App funcione
 */
const App = () => {
  console.log("Start App");
  addListeners();
  //Restablecemos la data
  data = JSON.parse(localStorage.getItem("data")) || {
    //Número aleatorio desde 1 hasta 1050
    limit: 4,
    favs: [],
    team: [],
  };

  data.offset = Math.floor(Math.random() * 1050) + 1;

  //Mostrando los FAVS y TEAM
  showListAsCard(data.favs, document.querySelector(".favs-result"));
  showListAsCard(data.team, document.querySelector(".team-result"));
  const endPoint =
    basePokeApi + `pokemon?limit=${data.limit}&offset=${data.offset}`;
  //Obteniendo la data discover
  getDiscoverPokemon(endPoint, saveDiscoverData);
};

//Cuando la ventana se cargue, no importa donde se ponga el script, funcionará
window.onload = App;
