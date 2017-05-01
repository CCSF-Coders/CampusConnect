import React from 'react';
import { connect } from 'react-redux';
import { setState } from '../../state';
import Header from '../../components/Header';

class FindClubs extends React.Component {
  render() {
    let { state } = this.props;
    console.log('find')
    return (
      <div>
        <Header />
        <h1>Find Clubs</h1>
        {state.clubs.map((club, i) => {
          return (
            <h3>{club.name}</h3>
          );
        })}
      </div>
    );
  }

  componentDidMount() {
    // fetch('http://127.0.0.1:8000/rest-api/clubs/?format=json')
    //   .then(res => res.json())
    //   .then(data => console.log('data', data))
    //   .catch(e => console.log('e', e));


      this.props.setState({ clubs: [ { id: 1, officers: [ ], members: [ ], name: "CCSF Coders", email: "", website: "", meeting_times: "" } ] });
  }
}

export default connect(
  state => ({ state }),
  dispatch => ({ setState: state => dispatch(setState(state)) })
)(FindClubs);
