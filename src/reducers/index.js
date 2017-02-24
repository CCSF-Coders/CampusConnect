import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux'

import {
  CREATE_EVENT
} from '../actions';

const rootReducer = combineReducers({
  routing: routerReducer,
  calendar: calendarReducer
});

function calendarReducer(state = null, action) {
  switch (action.type) {
    case CREATE_EVENT:
      return {
        ...state
      };
    default:
      return state;
  }
}

export default rootReducer;
