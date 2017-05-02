import React from 'react';
import { connect } from 'react-redux';
import { setState } from '../../state';

import './index.css';

class Login extends React.Component {
  render() {
    return (
      <div className="Login">
        <h1>CCSF Connect</h1>
        <h3>Discover, Interact, and Explore</h3>
        <p>An app created for CCSF Clubs</p>
        <div id="my-signin2"></div>
      </div>
    );
  }

  componentDidMount() {
    window.addEventListener('google-loaded', () => {
      this.props.setState({ googleLoaded: true });
      this.renderButton();
    });

    if (this.props.googleLoaded) {
      this.renderButton();
    }
  }

  renderButton() {
    console.log('rendering button')
    // https://developers.google.com/identity/sign-in/web/build-button
    window.gapi.signin2.render('my-signin2', {
      'scope': 'profile email',
      'width': 240,
      'height': 50,
      'longtitle': true,
      'theme': 'light',
      'onsuccess': this.onSignIn,
      'onfailure': e => console.log('error', e)
    });
  }

  onSignIn = googleUser => {
    this.props.setState({ user: googleUser.getBasicProfile() });
  }
}

export default connect(
  state => ({ state }),
  dispatch => ({ setState: state => dispatch(setState(state)) })
)(Login);
