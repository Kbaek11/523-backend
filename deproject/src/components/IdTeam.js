import React from 'react';
import ReactDOM from 'react-dom';

export default class IdTeam extends React.Component {
  state = {
    id: '',
    team: 'Basketball'
  };

  change = (e) => {
    this.setState ({
      [e.target.name]: e.target.value
    });
  }

  onSubmit = (e) => {
    e.preventDefault();
    this.props.onSubmit(this.state);
  }

  render() {
    return (
      <form>
        <input
        name = "id"
        placeholder="Unique Id #"
        value={this.state.id}
        onChange={e => this.change(e)}
        />

        <select name = "team" value = {this.state.team} onChange={e => this.change(e)}>
          <option value="Basketball">Basketball</option>
          <option value="Football">Football</option>
          <option value="Volleyball">Volleyball</option>
          <option value="Baseball">Baseball</option>
          <option value="Soccer">Soccer</option>
        </select>

        <button onClick={e => this.onSubmit(e)}>Submit</button>

      </form>
    );
  }
}
