import React, { useState, Component } from 'react';
import './components.css';
import { Routes,
  Route,
  useNavigate,
  useLocation,
  Navigate,Outlet, Link } from "react-router-dom";



export default function PopUp() {
  const navigate = useNavigate()
  const [username, setusername] = useState("");
  const [password, setpassword] = useState("");
  const [result, setresult] = useState("");

  const handleClick = () => {
    validate()
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: username , password: password})
    };
    fetch("/newuser", requestOptions)
    .then(response => response.json())
    .then(data => this.setState(data.result));
    // this.setState({email: val.currentTarget.value})
    console.log(result)
    navigate("/projectpage")
            
  };

function validate(){

};

      return (
        <div className= 'app'>
            <form>
            <div className="input-container">
              <label>New Username </label>
              <input type="text" name="uname" value = {username} id = "uname"  required onChange = {(e) => setusername(e.target.value) } />
            
          </div>
          <div className="input-container">
            <label>New Password </label>
            <input type="password" name="pass" value = {password} id = "pass" required onChange={(e) => setpassword(e.target.value)}/>
            
          </div>
          <div className="button-container">
          {/* <span onClick={handleClick} className="btn"> */}
          <span onClick={handleClick} className="btn">
              Submit
          </span>
            </div>
          </form>      
        </div>
      );
};



  
  
  
  