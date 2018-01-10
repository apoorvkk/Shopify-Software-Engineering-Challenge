import React, { Component } from 'react';
import { connect } from 'react-redux';

import submitProblem from '../actions/ProblemSender';
import { bindActionCreators } from 'redux';
import {
    MENUS_RESPONSE_SUCCESS,
    MENUS_RESPONSE_ERROR,
    MENUS_REQUEST_PENDING
} from '../actions/action-types';

class MenusProblemSubmitter extends Component {

    constructor(props) {
        super(props);
        this.state = {
            problemId: 1
        }
    }
    isRequestPending(){
        return this.props.processedMenus.status === MENUS_REQUEST_PENDING;
    }

    renderSubmitText() {
        if(this.isRequestPending()){
            return "Loading...";
        }
        return "Submit";
    }

    onChange = (event) => {
        this.setState({problemId: event.target.value});
    }

    onSubmit() {
        this.props.submitProblem(this.state.problemId);
    }

	render () {
		return (
        <div class="row">
            <div class="offset-sm-3 col-sm-6">
                <select onChange={this.onChange} id="problemId" class="selectpicker form-control">
                    <option>1</option>
                    <option>2</option>
                </select>
                <br />
                <span class="input-group-btn">
                    <button disabled={this.isRequestPending()} onClick={() => this.onSubmit()} class="btn btn-primary" type="submit">{this.renderSubmitText()}</button>
                </span>
            </div>
        </div>
		);
	}
}


function mapStateToProps(state) {
	return {
		processedMenus: state.processedMenus
	};
}

function mapDispatchToProps(dispatch) {
	return bindActionCreators({ submitProblem }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(MenusProblemSubmitter);
