import React from 'react';
import './index';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginScreen from './LoginScreen';
import NewProj from './NewProj';
import PopUp from './PopUp';

function App() {
  return (
    <>
      <Router>
        <Routes>
         <Route path='/' exact element={<LoginScreen />} /> 
         <Route path='/NewProj' element={<NewProj />} />
         <Route path='/PopUp' element={<PopUp />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
