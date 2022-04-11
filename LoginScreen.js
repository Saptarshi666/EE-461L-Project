import React, { useState, Component } from "react";
import './index.css';
import { Link } from "react-router-dom";




function LoginScreen({ isShowOrig, handleProjClick, handleUserClick}) {

  const [username, setusername] = useState("");
  const [password, setpassword] = useState(""); 
      
      
    const NewUserClick = () => {
        handleUserClick();
      };
    
    const handleClick = () => {
        validate();
        showAlert();
        handleProjClick();
                
      };

      const showAlert = () => {
        alert("I'm an alert");
      };
    
    function validate(){

    };
    
   
    return (
        <div className={`${isShowOrig ? "active" : ""} show`}>
        <form>
        <label>Sign In </label>
          <div className="input-container">
            <label>Username </label>
            <input type="text" name="uname" id = "uname" required onChange = {(e) => setusername(e.target.value)} />
            
          </div>
          <div className="input-container">
            <label>Password </label>
            <input type="password" name="pass" id = "pass" required onChange={(e) => setpassword(e.target.value)}/>
            
          </div>
          <div className="button-container">
          <span onClick={handleClick} className="btn">
              Submit
          </span>
          </div>
          <div>
          <span onClick={NewUserClick} className="btn">
              <Link to="/NewProj" onClick={handleClick}>
                New Project
              </Link>
          </span>
          </div>
          </form>      
      </div>
    );
    
}
  
  export default LoginScreen;