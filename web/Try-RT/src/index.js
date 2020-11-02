import React from "react";
import ReactDOM from "react-dom";
import List from "./containers/list";
import "bootstrap/dist/css/bootstrap.min.css";

const App = () => {
    return (
        <div className="container">
            <nav className="navbar stich-top navbar-light bg-dark">
                <h1 className="navbar-brand text-light">Movie List</h1>
            </nav>
            <List />
        </div>
    );
}

ReactDOM.render(< App/>, document.getElementById("root"));