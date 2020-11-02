import React, { Component } from "react";
import List from "./../list";
import "./App.css";

class App extends Component {
  constructor() {
    super();
    this.state = {
      title: "",
      tasks: [],
      id: 0,
    };
    // Esta instrucción debería ir por cada método (función) creada si no es arrow
    //this.onChange = this.onChange.bind(this);
  }

  onChange = (e) => {
    console.log(e);
    const value = e.target.value;
    this.setState({
      title: value,
    });
  };

  onSubmit = (e) => {
    e.preventDefault();

    const { title, tasks, id } = this.state;
    const newTask = {
      id,
      title,
    };

    this.setState({
      tasks: [...tasks, newTask],
      title: "",
      id: id + 1,
    });
  };

  onDelete = (id) => {
    const newTasks = this.state.tasks.filter((task) => task.id !== id);

    this.setState({
      tasks: newTasks,
    });
  };

  render() {
    return (
      <div>
        <form onSubmit={this.onSubmit}>
          <label htmlFor='title'>Título</label>
          <input id='title' value={this.state.title} onChange={this.onChange} />
          <button type='submit'>Agregar</button>
        </form>
        <List tasks={this.state.tasks} onDelete={this.onDelete} />
      </div>
    );
  }
}

export default App;
