import React from 'react';
import ReactDOM from 'react-dom';
//import {render} from 'react-dom';
//import {BrowserRouter as Router, Route} from "react-router-dom";

// import {Root} from "./components/Root";
// import {Form} from "./components/Form";

// import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();

// class App extends React.Component {
//   render() {
//     return (
//       <Router>
//         <Route path={"form"} component={Form}/>
//         <Route path={"home"} component={Home}/>
//       </Router>
//     );
//   }
// }
//
// render(<App />, window.document.getElementById('app'));
