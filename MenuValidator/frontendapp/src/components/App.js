import React, { Component } from 'react';

import MenusProblemSubmitter from './MenusProblemSubmitter';
import MenusSolution from './MenusSolution';

class App extends Component {
  render() {
    return (
      <div className="container">
        <div className="jumbotron">
          <h1 className="text-center">Menus Validator</h1>
          <hr />
          <p className="lead">
            Please select an existing problem instance id.
            The menus validator will then aggregate the products
            for that problem into valid and invalid menus.
          </p>

          <div className="row">
            <div className="col-sm-6">
              <MenusProblemSubmitter />
            </div>
            <div className="col-sm-6">
              <MenusSolution />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
