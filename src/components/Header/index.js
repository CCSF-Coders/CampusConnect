import React from 'react';
import { Link } from 'react-router-dom'
import { connect } from 'react-redux';
import { setState } from '../../state';
import './index.css';

class Header extends React.Component {
  render() {
    return (
      <div id="Header">
        <div style={{ flex: 1, alignItems: 'center' }}>
          <p className="button" onClick={() => this.signOut()}>Logout</p>
        </div>
        <div style={{ flex: 1, alignItems: 'center' }}>
          <Link to="/">
            <p className="button" onClick={() => {}}>Calendar</p>
          </Link>
        </div>
        <div style={{ flex: 1, alignItems: 'center' }}>
          <Link to="/findclubs">
            <p className="button" onClick={() => {}}>Find Clubs</p>
          </Link>
        </div>
        <div style={{ flex: 1, alignItems: 'center' }}>
          <Link to="/yourclubs">
            <p className="button" onClick={() => {}}>Your Clubs</p>
          </Link>
        </div>
      </div>
    );
  }

  signOut() {
    var auth2 = window.gapi.auth2.getAuthInstance();
    auth2.signOut().then(() => {
      console.log('User signed out.');
      this.props.resetUser();
    });
  }
}

export default connect(
  null,
  dispatch => ({ setState: state => dispatch(setState(state)) })
)(Header);
