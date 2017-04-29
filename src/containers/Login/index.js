import React from 'react';
import { connect } from 'react-redux';
import GoogleLogin from 'react-google-login';

import { setState } from '../../state';

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
    this.props.setState({ user: googleUser.getBasicProfile() });
  }
}

export default connect(
  state => ({ state }),
  dispatch => ({ setState: state => dispatch(setState(state)) })
)(Login);
