import React from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';

import Header from '../Header/index';

import { setUser } from '../../actions/index';

import './index.css';

class Login extends React.Component {
  render() {
    return (
      <div className="Welcome">
        <Header />
        <h1>Welcome</h1>
        <h1>{this.props.user.name}</h1>
      </div>
    );
  }
}

function mapStateToProps({ user }) {
  return {
    user
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators({
    setUser
  }, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(Login);
