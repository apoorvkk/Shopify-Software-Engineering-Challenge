import React, { Component } from 'react';
import MenusProblemSubmitter  from './MenusProblemSubmitter'
import MenusSolution from './MenusSolution'

class App extends Component {
  render() {
    return (
      <div class="container">
        <div class="jumbotron">
          <h1>Menus Validator</h1>
          <p class="lead">Please select an existing problem instance id. The menus validator will then aggregate the products for that problem into valid and invalid menus.</p>
          <MenusProblemSubmitter />
          <br />
          <MenusSolution />
        </div>
    </div>
    );
  }
}

export default App;
