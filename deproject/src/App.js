import React, {Component} from 'react';
import { BrowserRouter as Router, Link, NavLink} from 'react-router-dom';
import Route from 'react-router-dom/Route';
import './index.css';

import Home from "./components/Home";
import Form from "./components/Form";

const Main = () => {
  return ( <h1> Main Form </h1>);
}

export default class App extends Component {
  render() {
    return (
      <Router>
      <div className="App">
        <Link to="/form">Form</Link>

        <Route path="/" exact component={Home} />
        <Route path="/form" exact component={Form} />

      </div>
      </Router>
    );
  }
}
