import React from 'react';
import image from '../images/stabel.jpg';
import './App.css';


function App() {
  var path = "../images/stabel.jpg"
  var file = new File(path);
  var date = file.lastModifiedDate;
  return (
    <div className="App">
      <header className="App-header">
        <img src={path} className="App-logo" alt="logo" />
        <p>
          Date: {date}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
