import React from 'react';
import { Provider } from 'react-redux'
import { BrowserRouter, Route, Switch } from 'react-router-dom'

import Home from '../../containers/Home'
import FindClubs from '../../containers/FindClubs'
import YourClubs from '../../containers/YourClubs'
import { store } from '../../state';
import './index.css';


class App extends React.Component {
  render() {
    return (
      <Provider store={store}>
        <BrowserRouter>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/findclubs" component={FindClubs} />
            <Route path="/yourclubs" component={YourClubs} />
          </Switch>
        </BrowserRouter>
      </Provider>
    );
  }
}

export default App;
