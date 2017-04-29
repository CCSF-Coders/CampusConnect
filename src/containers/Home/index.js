import React from 'react';
import { connect } from 'react-redux';

import Login from '../../containers/Login';
import Welcome from '../../components/Welcome';
import { setState } from '../../state';

class Home extends React.Component {
  render() {
    let { state } = this.props;
    let Component = state.user ? Welcome : Login;
    return (
      <Component />
    );
  }
}

export default connect(
  state => ({ state }),
  dispatch => ({ setState: state => dispatch(setState(state)) })
)(Home);
