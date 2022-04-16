import React, { useState, Component } from 'react';
import './components.css';
import { Routes,
  Route,
  useNavigate,
  useLocation,
  Navigate,Outlet, Link } from "react-router-dom";



export default function Logout() {
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
    fetch("/logout", requestOptions)
    .then(response => response.json())
    .then(data => this.setState(data.result));
    // this.setState({email: val.currentTarget.value})
    console.log(result)
    navigate("/")
            
  };

function validate(){

};

      return (
        <div className= 'app'>
            <form>
        <span onClick={handleClick} className="btn">
              Log Out </span>
          </form>      
        </div>
      );
};