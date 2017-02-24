import React from 'react';

import './index.css';

class Home extends React.Component {
  render() {
    return (
      <div className="Container">
        <h1>CCSF Connect</h1>
        <h3>Discover, Interact, and Explore</h3>
        <p>An app created for CCSF Clubs</p>
        <div className="g-signin2" data-onsuccess={() => {console.log('signed in!')}}></div>
      </div>
    );
  }
}

export default Home;
