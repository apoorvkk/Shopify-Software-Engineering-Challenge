import {
	MENUS_IDLE,
	MENUS_RESPONSE_SUCCESS,
	MENUS_RESPONSE_ERROR,
	MENUS_REQUEST_PENDING
} from '../actions/action-types';

const initialState = {
	status: MENUS_IDLE,
	response: null
}
export default function(state=initialState, action){
	switch(action.type) {
		case MENUS_RESPONSE_SUCCESS:
			return {
				status: MENUS_RESPONSE_SUCCESS,
				response: action.payload,
			};
		case MENUS_RESPONSE_ERROR:
			return {
				status: MENUS_RESPONSE_ERROR,
				response: action.payload
			}
		case MENUS_REQUEST_PENDING:
			return {
				status: MENUS_REQUEST_PENDING,
				response: null
			}
	}
	return state;
}
