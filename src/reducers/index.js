import { combineReducers } from 'redux';
import { routerReducer } from 'react-router-redux'

import {
  SET_USER,
  CREATE_EVENT,
  RESET_USER,
  SET_GOOGLE_LOADED
} from '../actions';

const rootReducer = combineReducers({
  routing: routerReducer,
  user: userReducer,
  calendar: calendarReducer,
  googleLoaded: googleLoadedReducer
});

function userReducer(state = null, action) {
  switch (action.type) {
    case SET_USER:
      return {
        ...action.payload
      };
    case RESET_USER:
      return null;
    default:
      return state;
  }
}

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

function googleLoadedReducer(state = null, action) {
  switch (action.type) {
    case SET_GOOGLE_LOADED:
      return action.payload;
    default:
      return state;
  }
}

export default rootReducer;
