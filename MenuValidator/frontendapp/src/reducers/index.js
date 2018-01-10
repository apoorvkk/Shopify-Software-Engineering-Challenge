import { combineReducers } from 'redux';

import processedMenus from './reducer-processed-menus';

const rootReducer = combineReducers({
  processedMenus
});

export default rootReducer;
