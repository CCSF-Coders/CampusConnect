import React from 'react';
import { connect } from 'react-redux';
import { setState } from '../../state';
import Header from '../../components/Header';

class FindClubs extends React.Component {
  render() {
    // let { state } = this.props;
    console.log('find')
    return (
      <div>
        <Header />
        <h1>Find Clubs</h1>
      </div>
    );
  }
}

export default connect(
  state => ({ state }),
  dispatch => ({ setState: state => dispatch(setState(state)) })
)(FindClubs);
