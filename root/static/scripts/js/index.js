var React = require('react');

var Greeting = React.createClass ({
    // render() {
    //     return (<p>Hello world</p>);
    // }
      // updateLabel: fuction(event) {
      //   this.setState({value: event.target.value});
      // },

      getInitialState() {
        //set initial state of form inputs
        return {
          id: '',
          options: [{name:'Basketball'},
                    {name: 'Volleyball'},
                    {name: 'Soccer'},
                    {name: 'Tennis'},
                    {name: 'Football'}]
        }
      }

      ,render(){
        return(
          <div class="web-form">
          <form id="signin-form" onSubmit={this.handleSubmit}>
            <h2 className="form-signin-heading" >Sign in with your unique ID</h2>

            <div className="form-group has-success">
              <label htmlFor="id" className="sr-only">id</label>
              <input type="number" id="id" name="id" className="form-control" placeholder="id" onChange={this.handleidChange} required autoFocus />
            </div>
          </form>
        </div>
        )
      }
})
ReactDOM.render(
  <Greeting />,
  document.getElementById('form_container')
);
