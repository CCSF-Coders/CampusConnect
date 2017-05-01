import React from 'react';
import { connect } from 'react-redux';
import { setState } from '../../state';
import Header from '../../components/Header';

class YourClubs extends React.Component {
  render() {
    // let { state } = this.props;
    return (
      <div>
        <Header />
        <h1>Your Clubs</h1>
      </div>
    );
  }
}

export default connect(
  state => ({ state }),
  dispatch => ({ setState: state => dispatch(setState(state)) })
)(YourClubs);
