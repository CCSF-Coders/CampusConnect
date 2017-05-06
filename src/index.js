import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';

const root = document.getElementById('root');

ReactDOM.render(
  <App />,
  root
);

if (module.hot) {
  module.hot.accept('./components/App', () => {
    const NextApp = require('./components/App').default
    ReactDOM.render(
      <NextApp />,
      root
    )
  })
}
