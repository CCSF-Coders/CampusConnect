const SET_USER = 'SET_USER';
const RESET_USER = 'RESET_USER';
const CREATE_EVENT = 'CREATE_EVENT';
const SET_GOOGLE_LOADED = 'SET_GOOGLE_LOADED';

function setUser(user) {
  return {
    type: SET_USER,
    payload: user
  };
}

function resetUser() {
  return {
    type: RESET_USER
  };
}

function createEvent(event) {
  return {
    type: CREATE_EVENT,
    payload: event
  };
}

function setGoogleLoaded(boolean = false) {
  return {
    type: SET_GOOGLE_LOADED,
    payload: boolean
  };
}

export {
  setUser,
  SET_USER,
  resetUser,
  RESET_USER,
  createEvent,
  CREATE_EVENT,
  setGoogleLoaded,
  SET_GOOGLE_LOADED
};
