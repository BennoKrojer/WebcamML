import React from 'react';
import {ReactTitle} from 'react-meta-tags';
import MetaTags from 'react-meta-tags';
import './App.css';

var Date = require('./assets/date.json');
var RelPath = "images/current.jpg";

function App() {
  return (
    <div className="App">
      <meta http-equiv="refresh" content="180"/>
      <ReactTitle title="View of Munich, Germany"/>
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
