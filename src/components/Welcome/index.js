import React from 'react';
import { connect } from 'react-redux';
import BigCalendar from 'react-big-calendar';
import moment from 'moment';

import Header from '../Header';
import { setState } from '../../state';

import './index.css';
import 'react-big-calendar/lib/css/react-big-calendar.css';

BigCalendar.momentLocalizer(moment)

class Login extends React.Component {
  render() {
    let { state } = this.props;
    return (
      <div className="Welcome">
        <Header />
        {/* <h1>Welcome</h1>
        <h1>{state.user.name}</h1> */}
        <div style={{ border: '1px solid black', width: '900px', height: '500px' }}>
          <BigCalendar
            events={[]}
          />
        </div>
      </div>
    );
  }
}

export default connect(
  state => ({ state }),
  dispatch => ({ setState: state => dispatch(setState(state)) })
)(Login);
