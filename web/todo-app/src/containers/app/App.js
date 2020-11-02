import React, {Component} from 'react';
import List from "./../list";
import "./App.css";

class App extends Component {
  constructor(){
    super();
    this.state = {
      title:'',
    };
    // Esta instrucción debería ir por cada método (función) creada si no es arrow
    //this.onChange = this.onChange.bind(this);
  }

  onChange = (e) => {
    console.log(e);
    const value = e.target.value;
    this.setState({
      title:value,
    });
  } 

  render () {
    return (
      <div>
        <form>
          <dl>
            <dt>
              <label htmlFor='title'>Título</label>
            </dt>
            <dt>
              <input id='title' value={this.state.title} onChange={this.onChange}/>
            </dt>
          </dl>
          <button type='submit'>Agregar</button>
        </form>
        <List />
      </div>
    );
  }

}

export default App;
