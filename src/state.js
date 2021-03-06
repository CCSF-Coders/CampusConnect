
import { createStore } from 'redux';
const SET_STATE = 'SET_STATE';

const defaultState = {
  user: null,
  clubs: [],
  googleLoaded: false
};

const setState = function(state) {
  return {
    type: SET_STATE,
    payload: state
  };
}

const stateReducer = function(state = defaultState, action) {
  switch (action.type) {
    case SET_STATE:
      return {
        ...state,
        ...action.payload
      };
    default:
      return state;
  }
}

const store = createStore(stateReducer);

export {
  setState,
  store
};
