const CREATE_EVENT = 'CREATE_EVENT';

function createEvent(event) {
  return {
    type: CREATE_EVENT,
    payload: event
  };
}

export {
  createEvent,
  CREATE_EVENT
};
