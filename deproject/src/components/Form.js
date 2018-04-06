import React from 'react';
import ReactDOM from 'react-dom';

export default class Form extends React.Component {
  render() {
    return (
      <div class="container main-form">
        <div class="row">
          <div class="col">
            <h2>1. Alcohol Consumption in the Past 2 Weeks</h2>
            <p>For A, did you consume alcohol for that day? Please state Yes or No.</p>
            <p>For B, approximately how many drinks did you consume? Please input your amount in whole numbers.</p>
            <p>For C, for how long did you consume these drinks (unit: hours)? Please input your amount in whole numbers.</p>
          </div>
        </div>
        <div class="row">
          <div class="col">
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

          </div>
        </div>
        <div class="row">
          <div class="col">
            <h2>2. Brief Young Adult Alcohol Consequences Questionnaire</h2>
            <p>
              Below is a list of things that sometimes happen to people either during or after they have been drinking alcohol.  Next to each item below, please mark an “X” in either the NO or the YES column to indicate whether that item describes something that has happened to you IN THE PAST YEAR.
            </p>
          </div>
        </div>

        <div class="row">
          <div class="col">
          <table>
            <tr>
              <th>In the past year...</th>
              <th>YES</th>
              <th>NO</th>
            </tr>
            <tr>
              <td>1. I have had a hangover (headache, sick stomach) the morning after I had been drinking.</td>
              <td><input type="checkbox" name="yes" />&nbsp;</td>
              <td><input type="checkbox" name="no" />&nbsp;</td>
            </tr>
            <tr>
              <td>2. I have taken foolish risks when I have been drinking.</td>
              <td><input type="checkbox" name="yes" />&nbsp;</td>
              <td><input type="checkbox" name="no" />&nbsp;</td>
            </tr>
            <tr>
              <td>3. I’ve not been able to remember large stretches of time while drinking heavily.</td>
              <td><input type="checkbox" name="yes" />&nbsp;</td>
              <td><input type="checkbox" name="no" />&nbsp;</td>
            </tr>
            <tr>
              <td>4. The quality of my work or school work has suffered because of my drinking.</td>
              <td><input type="checkbox" name="yes" />&nbsp;</td>
              <td><input type="checkbox" name="no" />&nbsp;</td>
            </tr>
            <tr>
              <td>5. I have had less energy or felt tired because of my drinking.</td>
              <td><input type="checkbox" name="yes" />&nbsp;</td>
              <td><input type="checkbox" name="no" />&nbsp;</td>
            </tr>
            <tr>
              <td>6. My drinking has gotten me into sexual situations I later regretted.</td>
              <td><input type="checkbox" name="yes" />&nbsp;</td>
              <td><input type="checkbox" name="no" />&nbsp;</td>
            </tr>
            <tr>
              <td>7. I often have ended up drinking on nights when I had planned not to drink.</td>
              <td><input type="checkbox" name="yes" />&nbsp;</td>
              <td><input type="checkbox" name="no" />&nbsp;</td>
            </tr>
            <tr>
              <td>8. My physical appearance has been harmed by my drinking.</td>
              <td><input type="checkbox" name="yes" />&nbsp;</td>
              <td><input type="checkbox" name="no" />&nbsp;</td>
            </tr>
            <tr>
              <td>9. While drinking, I have said or done embarrassing things.</td>
              <td><input type="checkbox" name="yes" />&nbsp;</td>
              <td><input type="checkbox" name="no" />&nbsp;</td>
            </tr>
            <tr>
              <td>10. I have felt very sick to my stomach or thrown up after drinking.</td>
              <td><input type="checkbox" name="yes" />&nbsp;</td>
              <td><input type="checkbox" name="no" />&nbsp;</td>
            </tr>
          </table>
          </div>
        </div>

        <div class="row">
          <div class="col">
            <div className="App">
              
            </div>
          </div>
        </div>

      </div>
    );
  }
}
