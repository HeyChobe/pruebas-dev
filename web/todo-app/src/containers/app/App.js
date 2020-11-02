import React, { useState } from "react"; //Usando hooks
import List from "./../list";
import "./App.css";

function App() {

  //Los Hooks me sirven como "estados" pero dentro de funciones
  //Debo crear uno por cada elemento del estado que necesito
  //const [valor, función_para_modificar_valor] = useState(valor_defecto)

  const [title, setTitle] = useState("");
  const [id, setId] = useState(0);
  const [tasks, setTasks] = useState([]);
  
  const onChange = (e) => {
    const value = e.target.value;
    setTitle(value);
  };

  const onSubmit = (e) => {
    e.preventDefault();

    const newTask = {
      id,
      title,
    };

    setTasks([...tasks, newTask]);
    setTitle("");
    setId(id+1);
  };

   const onDelete = (id) => {
    const newTasks = tasks.filter((task) => task.id !== id);
    setTasks(newTasks);
  };

  return (
    <div>
      <form onSubmit={onSubmit}>
        <label htmlFor='title'>Título</label> 
        <input id='title' value={title} onChange={onChange} />
        <button type='submit'>Agregar</button>
      </form>
      <List tasks={tasks} onDelete={onDelete} />
    </div>
  );
}

export default App;
