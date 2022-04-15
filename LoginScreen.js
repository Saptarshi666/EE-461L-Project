import React, { useState } from "react";
import './components.css';
import { Routes,
  Route,
  useNavigate,
  useLocation,
  Navigate,Outlet, Link } from "react-router-dom";
import { useEffect } from "react";



export default function LoginScreen() {
  const navigate = useNavigate()
  const [username, setusername] = useState("");
  const [password, setpassword] = useState("");
  const [result, setresult] = useState([]);
   
  const handleClick = () => {
    validate()
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: username , password: password})
    };
    fetch("/login", requestOptions)
    .then(response => response.json())
    .then(data => console.log(data.result));
    // this.setState({email: val.currentTarget.value})
    console.log('data')
    console.log(result)
    navigate("/Datasets")
  };

  // const handleClick = () => {
  //   useEffect(() => {
  //     // POST request using fetch inside useEffect React hook
  //     const requestOptions = {
  //         method: 'POST',
  //         headers: { 'Content-Type': 'application/json' },
  //         body: JSON.stringify({ username: username, password: password })
  //     };
  //     fetch('/login', requestOptions)
  //         .then(response => response.json())
  //         .then(data => setresult(data.result));
  //         console.log(response)
  
  // // empty dependency array means this effect will only run once (like componentDidMount in classes)
  // }, []);
  // };

    function validate(){

    };
    
   
    return (
        <div className= 'app'>
        <form>
        <label>Sign In </label>
          <div className="input-container">
            <label>Username </label>
            <input type="text" name="uname" value={username} id = "uname" required onChange = {(e) => setusername(e.target.value)} />
          </div>
          <div className="input-container">
            <label>Password </label>
            <input type="password" name="pass" value={password} id = "pass" required onChange={(e) => setpassword(e.target.value)}/>
            
          </div>
          <div className="button-container">
          <span onClick={handleClick} className="btn">
              Submit
          </span>
          </div>
          
          </form>      
      </div>
    );
    
}
  
  