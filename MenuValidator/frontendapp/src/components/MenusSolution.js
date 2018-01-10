import React, { Component } from 'react';
import { connect } from 'react-redux';
import JSONPretty from 'react-json-pretty';

import {
  MENUS_REQUEST_PENDING,
  MENUS_IDLE,
  MENUS_RESPONSE_ERROR
} from '../actions/action-types';

class MenusSolution extends Component {
  showResponseData() {
    if (this.props.processedMenus.status !== MENUS_REQUEST_PENDING && this.props.processedMenus.status !== MENUS_IDLE) {
      return this.props.processedMenus.response;
    }
    return {};
  }

  render() {
    if(this.props.processedMenus.status === MENUS_RESPONSE_ERROR) {
      return (
        <div style={{color: 'red'}}>
          {this.showResponseData()}
        </div>
      );
    }
    return (<JSONPretty id="json-pretty" style={{border: '1px solid black', 'background-color': 'white'}} json={this.showResponseData()}></JSONPretty>);
  }
}

function mapStateToProps(state) {
  return {
    processedMenus: state.processedMenus
  };
}

export default connect(mapStateToProps)(MenusSolution);
