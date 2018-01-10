import {
	MENUS_RESPONSE_SUCCESS,
	MENUS_RESPONSE_ERROR,
	MENUS_REQUEST_PENDING
} from './action-types';
import axios from 'axios';

export default function submitProblem(problemId) {
  return (dispatch) => {
    const success = (res) => {
      console.log(res.data);
        dispatch({
        	type: MENUS_RESPONSE_SUCCESS,
        	payload: res.data
       	});
    };
    const fail =  (err) => {
        dispatch({
          type: MENUS_RESPONSE_ERROR,
          payload: err.toString()
        });
    };
    const url = 'https://menu-validator-backend.herokuapp.com/fetch-menus?problem-id=' + problemId.toString()

    dispatch({
      type: MENUS_REQUEST_PENDING
    });

    axios.get(url)
    	.then(success)
    	.catch(fail);
  };
}
