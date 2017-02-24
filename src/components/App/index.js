import React from 'react';
import { createStore } from 'redux'
import { Provider } from 'react-redux'
import { Router, Route, browserHistory } from 'react-router'
import { syncHistoryWithStore } from 'react-router-redux'

import Home from '../../containers/Home/index'

import rootReducer from '../../reducers/index';

import './index.css';

const store = createStore(rootReducer);
const history = syncHistoryWithStore(browserHistory, store)

class App extends React.Component {
  render() {
    return (
      <Provider store={store}>
        <Router history={history}>
          <Route path="/" component={Home}></Route>
        </Router>
      </Provider>
    );
  }
}

export default App;
