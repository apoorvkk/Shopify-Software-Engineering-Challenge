import React, { Component } from 'react';
import { connect } from 'react-redux';
import ReactJson from 'react-json-view'
import {
    MENUS_RESPONSE_SUCCESS,
    MENUS_RESPONSE_ERROR,
    MENUS_REQUEST_PENDING,
    MENUS_IDLE
} from '../actions/action-types';

class MenusSolution extends Component {

    getJsonData() {
        if(this.props.processedMenus.status !== MENUS_REQUEST_PENDING && this.props.processedMenus.status !== MENUS_IDLE) {
            return this.props.processedMenus.response;
        }
        return {};
    }

	render () {
	   return ( <ReactJson src={this.getJsonData()} theme="shapeshifter:inverted" /> );
	}
}


function mapStateToProps(state) {
	return {
		processedMenus: state.processedMenus
	};
}

export default connect(mapStateToProps)(MenusSolution);
