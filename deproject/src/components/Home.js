import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Link, NavLink} from 'react-router-dom';
// import './index.css';
import IdTeam from './IdTeam';

export default class Home extends React.Component {
  state = {
    fields: {}
  };

  onSubmit = (fields) => {
  this.setState({ fields });
  };

  render() {
    return (
      <div class="container-fluid">
      <div id="root" class="row home">
        <div class="unc-background">
          <img src="/images/ramses.jpg" alt="UNC mascot Ramses" />
        </div>
        <div class="description">
          <h1>Drug Education Program</h1>
          <br />
          <p>
          This short program will ask you questions about how much alcohol you drink and which drugs you use (illegal, prescription, and over-the-counter). When you are finished, you’ll instantly get a response with information specific to what you answered. Your information can help you increase your health and improve your athletic performance.
          </p>
          <br />
          <div id="home-button">
          <h2>Enter your <span title="The number you got from the Athletics Dept email">Unique ID Number</span></h2>
            <IdTeam onSubmit={fields => this.onSubmit(fields)}/>
            <p>{JSON.stringify(this.state.fields, null, 2)}</p>
          </div>
        </div>
      </div>
    </div>
    );
  }
}
