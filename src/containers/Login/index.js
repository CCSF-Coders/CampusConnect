import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import GoogleLogin from 'react-google-login';

import { setUser, setGoogleLoaded } from '../../actions';

import './index.css';

class Login extends React.Component {
  render() {
    return (
      <div className="Login">
        <h1>CCSF Connect</h1>
        <h3>Discover, Interact, and Explore</h3>
        <p>An app created for CCSF Clubs</p>
        <GoogleLogin
          clientId="310141997963-25c8dvqieo2um40i81s6is01u7ivlcjr.apps.googleusercontent.com"
          buttonText="Login"
          onSuccess={this.onSignIn}
          onFailure={e => console.log('e', e)}
        />
      </div>
    );
  }

  onSignIn = googleUser => {
    console.log('googleUser', googleUser)
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
