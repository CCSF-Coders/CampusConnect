import React from 'react';
import { Provider } from 'react-redux'
import { Route } from 'react-router'
import { BrowserRouter } from 'react-router-dom'

import Home from '../../containers/Home'
import { store } from '../../state';
import './index.css';


class App extends React.Component {
  render() {
    return (
      <Provider store={store}>
        <BrowserRouter>
          <Route path="/" component={Home}></Route>
        </BrowserRouter>
      </Provider>
    );
  }
}

export default App;
