import React from 'react';
import { Link } from 'react-router-dom'
import { connect } from 'react-redux';
import { setState } from '../../state';
import './index.css';

class Header extends React.Component {
  componentWillMount() {
    if (!this.props.state.user) {
      window.location.replace('http://localhost:3000/');
    }
  }

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
    var auth = window.gapi.auth2.getAuthInstance();
    auth.signOut().then(() => {
      this.props.setState({ user: null });
      window.location.replace('http://localhost:3000/');
    });
  }
}

export default connect(
  state => ({ state }),
  dispatch => ({ setState: state => dispatch(setState(state)) })
)(Header);
