import React from 'react';
import ReactDOM from 'react-dom';

export default class One extends React.Component {
  state = {
    day1A: '',
    day1B: '',
    day1C: '',
    day2A: '',
    day2B: '',
    day2C: '',
    day3A: '',
    day3B: '',
    day3C: '',
    day4A: '',
    day4B: '',
    day4C: '',
    day5A: '',
    day5B: '',
    day5C: '',
    day6A: '',
    day6B: '',
    day6C: '',
    day7A: '',
    day7B: '',
    day7C: '',
    day8A: '',
    day8B: '',
    day8C: '',
    day9A: '',
    day9B: '',
    day9C: '',
    day10A: '',
    day10B: '',
    day10C: '',
    day11A: '',
    day11B: '',
    day11C: '',
    day12A: '',
    day12B: '',
    day12C: '',
    day13A: '',
    day13B: '',
    day13C: '',
    day14A: '',
    day14B: '',
    day14C: '',
  };

  change = (e) => {
    this.setState ({
      [e.target.name]: e.target.value
    });
  }

  onOneSubmit = (e) => {
    e.preventDefault();
    this.props.onOneSubmit(this.state);
  }

  render() {
    return (
      <form>
      <table class="calendar">
        <tr>
          <th>Sunday</th>
          <th>Monday</th>
          <th>Tuesday</th>
          <th>Wednesday</th>
          <th>Thursday</th>
          <th>Friday</th>
          <th>Saturday</th>
        </tr>
        <tr>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
        </tr>
        <tr>
          <th>Sunday</th>
          <th>Monday</th>
          <th>Tuesday</th>
          <th>Wednesday</th>
          <th>Thursday</th>
          <th>Friday</th>
          <th>Saturday</th>
        </tr>
        <tr>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
          <td>
            <input text="text" placeholder="A"/>
            <input text="number" placeholder="B"/>
            <input text="number" placeholder="C"/>
          </td>
        </tr>
      </table>

      <button onClick={e => this.onOneSubmit(e)}>Submit</button>
      </form>
    );
  }
}
