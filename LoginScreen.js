import React, { useState, Component } from "react";
import './index.css';




function LoginScreen({ isShowOrig, handleSubmitClick, handleUserClick}) {

  const [username, setusername] = useState("");
  const [password, setpassword] = useState("");
      
      
    const NewUserClick = () => {
        handleUserClick();
      };
    
    const handleClick = () => {
        validate()
        handleSubmitClick();
                
      };
    
    function validate(){

    };
    
   
    return (
        <div className={`${isShowOrig ? "active" : ""} show`}>
        <form onSubmit={handleClick}>
          <div className="input-container">
            <label>Username </label>
            <input type="text" name="uname" id = "uname" required onChange = {(e) => setusername(e.target.value)} />
            
          </div>
          <div className="input-container">
            <label>Password </label>
            <input type="password" name="pass" id = "pass" required onChange={(e) => setpassword(e.target.value)}/>
            
          </div>
          <div className="button-container">
            <input type="submit"  />
          </div>
          <div>
          <span onClick={NewUserClick} className="btn">
              New User
          </span>
          </div>
        </form>      
      </div>
    );
    
}
  
  export default LoginScreen;