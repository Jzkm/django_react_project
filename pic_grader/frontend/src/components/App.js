import React, { Component } from 'react';
import { render } from 'react-dom';
import HomePage from './HomePage';
import { BrowserRouter as Router, Route,Routes} from 'react-router-dom';
import { createRoot } from 'react-dom/client';
import PicChoose from "./PicChoose"
import Test from "./Test"
import Create_Exhibition from './CreateExhibition'


export default function App() {
    return (
      <div className='git'>
        <Router >
          <Routes>
            <Route exact path="/" element={<HomePage />} />
            <Route exact path="/Picgrader" element={<PicChoose />} />
            <Route exact path="/test" element={<Test />} />
            <Route path="/Picgrader/:ppCodes" element={<PicChoose />} />
            <Route exact path="/Create_Exhibition" element={<Create_Exhibition />} />
          </Routes>
        </Router>
      </div>
    )
  }


// const appDiv = document.getElementById('app');
// render(<App />,appDiv)
const root = createRoot(document.getElementById('app')); // Wskazuje na element HTML, w którym chcesz umieścić aplikację
root.render(<App />);