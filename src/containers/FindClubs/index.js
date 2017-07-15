import React from 'react';
import { connect } from 'react-redux';
import { setState } from '../../state';
import Header from '../../components/Header';

class FindClubs extends React.Component {
  render() {
    let { state } = this.props;

    return (
      <div>
        <Header />
        <h1>Find Clubs</h1>
        {state.clubs.map((club, i) => {
          return (
            <h3 key={i}>{club.name}</h3>
          );
        })}
      </div>
    );
  }

  componentDidMount() {
    fetch('http://127.0.0.1:8000/rest-api/clubs/?format=json')
      .then(res => res.json())
      .then(clubs => {
        console.log('CLUBS', clubs);
        this.props.setState({ clubs });
      })
      .catch(e => console.log('e', e));
  }
}

export default connect(
  state => ({ state }),
  dispatch => ({ setState: state => dispatch(setState(state)) })
)(FindClubs);
