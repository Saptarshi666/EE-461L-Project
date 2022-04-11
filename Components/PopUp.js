import React, { useState, Component } from 'react';
import './components.css';


export default function PopUp() {
  const [username, setusername] = useState("");
  const [password, setpassword] = useState("");

  const handleClick = () => {
    validate()
   
            
  };

function validate(){

};

      return (
        <div className= 'app'>
            <form>
            <div className="input-container">
              <label>New Username </label>
              <input type="text" name="uname" id = "uname" required onChange = {(e) => setusername(e.target.value)} />
            
          </div>
          <div className="input-container">
            <label>New Password </label>
            <input type="password" name="pass" id = "pass" required onChange={(e) => setpassword(e.target.value)}/>
            
          </div>
          <div className="button-container">
          <span onClick={handleClick} className="btn">
              Submit
          </span>
            </div>
          </form>      
        </div>
      );
};



  
  
  
  