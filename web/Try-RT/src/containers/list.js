import React, { Component } from "react"; //Clase component
import Card from "./../components/cards/card";

class List extends Component {
    constructor(){
        super(); //Siempre lo llamo
        this.state = {
            data: [],
            loading: true,
        }; //Importante crear el estado
    };
    //Cuando el componente está siendo montada
    async componentDidMount () {
        const movies = await fetch('assets/data.json');
        const moviesJSON = await movies.json();

        //Modifico el objeto atómicamente
        if(moviesJSON){
            this.setState({
                data: moviesJSON,
                loading: false
            });
        }
    }
    render(){
        const {data, loading} = this.state;
        if(loading){
            return <div>Loading...</div>
        }
        return(
            <div className="row">
                {data.map(movie => <Card key={movie.id} movie={movie}/>)};
            </div>
        )
    }
}

//Para al importar este archivo se importe la clase
export default List;