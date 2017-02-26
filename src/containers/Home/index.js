import React from 'react';
import { connect } from 'react-redux';

import Login from '../../containers/Login';
import Welcome from '../../components/Welcome';

class Home extends React.Component {
  render() {
    let Component = this.props.user ? Welcome : Login;
    console.log('THIS.PROPS.USER', this.props.user)
    return (
      <Component />
    );
  }
}

function mapStateToProps({ user }) {
  return {
    user
  };
}

export default connect(mapStateToProps)(Home);
