import React, { useState, Component } from 'react';
import './index.css';



function PopUp({ isShowLogin, handleSubmitClick}) {
  const [username, setusername] = useState("");
  const [password, setpassword] = useState("");

  const handleClick = () => {
    validate()
    handleSubmitClick();
            
  };

function validate(){

};

      return (
        <div className={`${isShowLogin ? "active" : ""} show`}>
            <form onSubmit={handleClick}>
            <div className="input-container">
              <label>New Username </label>
              <input type="text" name="uname" id = "uname" required onChange = {(e) => setusername(e.target.value)} />
            
          </div>
          <div className="input-container">
            <label>New Password </label>
            <input type="password" name="pass" id = "pass" required onChange={(e) => setpassword(e.target.value)}/>
            
          </div>
            <div className="button-container">
              <input type="submit" />
            </div>
          </form>      
        </div>
      );
};

export default PopUp;

  
  
  
  