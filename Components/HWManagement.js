import React,{ Component, useState } from 'react'
import "./components.css";
import { Routes,
	Route,
	useNavigate,
	useLocation,
	Navigate,Outlet, Link } from "react-router-dom";

export default function HWManagement() {

const [units, setunits] = useState("")
const [hwset, sethwset] = useState("")
const [proj, setproj] = useState("")
const navigate = useNavigate()
// Form submitting logic


// Method causes to store all the values of the
// input field in react state single method handle
function handleCheckin() {
	
	navigate("/projdetails")
	
}

function handleCheckout() {
	
	navigate("/projdetails")
	
}

// Return a controlled form i.e. values of the
// input field not stored in DOM values are exist
// in react component itself as state

	
	return(
	<div classname = "app">
		<form>
		<div>
		<label>Current Funds </label>
		
		<div className="input-container">
            <label>Project </label>
            <input type="text" name="proj" id = "proj" required onChange = {(e) => setproj(e.target.value)} />
		</div>
		</div>
		
		<div>
		<div className="input-container">
            <label>Hardware Set </label>
            <input type="text" name="hwset" id = "hwset" required onChange = {(e) => sethwset(e.target.value)} />
		</div>
		</div> 
		
	
		
		
        <div>
		<div className="input-container">
            <label>Units </label>
            <input type="text" name="units" id = "units" required onChange = {(e) => setunits(e.target.value)} />
		</div>
		</div>
		<div className="button-container">
          <span onClick={handleCheckin} className="btn">
              Check In
          </span>
		  <span onClick={handleCheckout} className="btn">
              Check Out
          </span>
		  
		</div>
		</form>
		</div>
	
	)
}



