import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { resetUser } from '../../actions';
import './index.css';

class Header extends React.Component {
  render() {
    return (
      <div id="Header">
        <div style={{ flex: 1 }}>
          <p onClick={() => this.signOut()}> Logout </p>
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

function mapDispatchToProps(dispatch) {
  return bindActionCreators(
    {
      resetUser
    },
    dispatch
  );
}

export default connect(null, mapDispatchToProps)(Header);
