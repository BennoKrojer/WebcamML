import React from 'react';
import './App.css';

var Date = require('./assets/date.json');
var RelPath = "images/current.jpg";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img width="1194" height="672" src={RelPath} className="webcam-image" alt="View of Munich, Germany including the Frauenkirche, Staatsoper, Theatinerkirche and Olympiapark." />
        <p>
          Date: {Date.string}
        </p>
      </header>
    </div>
  );
}

export default App;
