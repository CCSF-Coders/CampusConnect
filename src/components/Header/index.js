import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { resetUser } from '../../actions';
import './index.css';

class Header extends React.Component {
  render() {
    return (
      <div id="Header">
        <p> CampusConnect </p>
        <p> Edit Profile </p>
        <p> Calendars </p>
        <p> Browse Clubs </p>
        <div class="form-group" id="form-margin">
          <input type="text" class="form-control" placeholder="Search For Clubs" id="form-length"/>
        </div>
        <button type="Submit" className="btn btn-default"> Submit </button>
        <p> Member Requests </p>
        <p onClick={() => this.signOut()}> Logout </p>
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
  return bindActionCreators({
    resetUser
  }, dispatch);
}

export default connect(null, mapDispatchToProps)(Header);
