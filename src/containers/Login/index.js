import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import { setUser, setGoogleLoaded } from '../../actions/index';

import './index.css';

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.renderButton = this.renderButton.bind(this);
    this.onSignIn = this.onSignIn.bind(this);
  }

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
    console.log('componentDidMount')
    window.addEventListener('google-loaded', () => {
      this.props.setGoogleLoaded(true);
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

  onSignIn(googleUser) {
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    this.props.setUser({
      id: profile.getId(),
      name: profile.getName(),
      imageUrl: profile.getImageUrl(),
      email: profile.getEmail()
    });
  }
}

function mapStateToProps({ googleLoaded }) {
  return {
    googleLoaded
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators({
    setUser,
    setGoogleLoaded
  }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(Login);
