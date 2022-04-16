import React, { useState, Component } from "react";
import './components.css';
import { useNavigate } from "react-router-dom";




function HWManagement() {
  const navigate = useNavigate()
  const [setName, sethwsetname] = useState("");
//   const [action, setaction] = useState("");
  const [capacity, setcapacity] = useState("");
  const [availablity, setavailablity] = useState("");
  const [projID, setprojid] = useState("");
  const [amount, setamount] = useState("");
  const [result, setresult] = useState("");
  const [availablity1, setavailablity1] = useState("");
  const [hwresult, sethwresult] = useState("");
  const [hwset1, sethwset1] = useState("");
  const [hwset2, sethwset2] = useState("");
  
    function GetAvailablityHW1(){
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ setName: 'HWSet1'})
      };
      fetch("/HWManagement", requestOptions)
      .then(response => response.json())
      .then(data => setavailablity(data.result));
      // this.setState({email: val.currentTarget.value})
      console.log(availablity)
      navigate("/HWManagement")       
    }
	function GetAvailablityHW2(){
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ setName: 'HWSet2'})
    };
    fetch("/HWManagement", requestOptions)
    .then(response => response.json())
    .then(data => setavailablity1(data.result));
    // this.setState({email: val.currentTarget.value})
    console.log(availablity1)
    navigate("/HWManagement")       
	  }
  function checkinHW1(){
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({  projID: projID,amount:  amount, setName:'HWSet1'})
    };
    fetch("/HWManagement2", requestOptions)
    .then(response => response.json())
    .then(data => setavailablity(data.result));
    // this.setState({email: val.currentTarget.value})
    console.log(availablity)
    if(availablity == "noprojerror"){
      alert("This project does not exist right now")
    }
    if(availablity == "toomany"){
      alert("You are trying to check in more sets than you have checked out. Try again")
    }
    navigate("/HWManagement")
  }
  function checkinHW2(){
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({  projID: projID,amount:  amount, setName:'HWSet2'})
    };
    fetch("/HWManagement2", requestOptions)
    .then(response => response.json())
    .then(data => setavailablity1(data.result));
    // this.setState({email: val.currentTarget.value})
    console.log(availablity1)
    if(availablity1 == "noprojerror"){
      alert("This project does not exist right now")
    }
    if(availablity1 == "toomany"){
      alert("You are trying to check in more sets than you have checked out. Try again")
    }
    navigate("/HWManagement")
  }  
  function checkoutHW2(){
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({  projID: projID,amount:  amount, setName:'HWSet2'})
    };
    fetch("/HWManagement1", requestOptions)
    .then(response => response.json())
    .then(data => setavailablity1(data.result));
    // this.setState({email: val.currentTarget.value})
    console.log(availablity1)
    if(availablity1 == "noprojerror"){
      alert("This project does not exist right now")
    }
    if(availablity1 == "noseterror"){
      alert("no such set exists")
    }
    if(availablity1 == "noneavailable"){
      alert("none of these sets are available right now")
    }
    navigate("/HWManagement")
  }  
  function checkoutHW1(){
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({  projID: projID,amount:  amount, setName:'HWSet1'})
    };
    fetch("/HWManagement1", requestOptions)
    .then(response => response.json())
    .then(data => setavailablity(data.result));
    // this.setState({email: val.currentTarget.value})
    console.log(availablity)
    if(availablity == "noprojerror"){
      alert("This project does not exist right now")
    }
    if(availablity == "noseterror"){
      alert("no such set exists")
    }
    if(availablity == "noneavailable"){
      alert("none of these sets are available right now")
    }
    navigate("/HWManagement")
  }  
  function GetProjectHardware(){
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({  projID: projID})
    };
    fetch("/projectHW", requestOptions)
    .then(response => response.json())
    .then(data => sethwresult(data));
    // this.setState({email: val.currentTarget.value})
    sethwset1(hwresult["set1"])
    sethwset2(hwresult["set2"])
    if(hwresult["result"] == "noprojerror"){
      alert("This project does not exist right now")
    }
    console.log(hwresult)
    console.log(hwset1)
    console.log(hwset2)
    navigate("/HWManagement")
  } 
    // function OpenExistingClick(){
    //   const requestOptions = {
    //     method: 'POST',
    //     headers: { 'Content-Type': 'application/json' },
    //     body: JSON.stringify({projID: projID})
    //   };
    //   fetch("/projectpage", requestOptions)
    //   .then(response => response.json())
    //   .then(data => this.setState(data.result));
    //   // this.setState({email: val.currentTarget.value})
    //   console.log(result)
    //   navigate("/HWManagement")       
    // }
     
      
   
    return (
     
       
      <div className='app3'>
          <div>
          <form>
          <label>HWSet1</label>
		  	<label>Capacity: 100 </label>
			  <label>Availability: </label>
			  <span onClick={GetAvailablityHW1} className="btn">
              Get Availablity HW1 {availablity} </span>
              <label>HWSet2</label>
		  	<label>Capacity: 100 </label>
			  <label>Availability: </label>
        <span onClick={GetAvailablityHW2} className="btn">
              Get Availablity HW2 {availablity1} </span>
        <label>Project ID </label>
            <input type="text" name="projID" value={projID} id = "projID" required onChange = {(e) => setprojid(e.target.value)} />
              <label><br/>HWSet1 Out:  {hwset1}<br /></label>
              <label>HWSet2 Out: {hwset2}<br /></label>
        <span onClick={GetProjectHardware} className="btn">
              Get Project Hardware </span>
              <label> Amount</label>
        <input type="amount" name="amount" value={amount} id = "amount" required onChange={(e) => setamount(e.target.value)}/>
        <span onClick={checkinHW1} className="btn">
              checkin HW1  </span>  
        <span onClick={checkinHW2} className="btn">
              checkin HW2  </span>
        <span onClick={checkoutHW1} className="btn">
              checkout HW1  </span>  
        <span onClick={checkoutHW2} className="btn">
              checkout HW2  </span>
          </form>
          </div>
         
         <div></div>
         
         <div >
           <form>

          </form>
          </div>    
      </div>
     
    );
    
}
  
  export default HWManagement;

{/* <label htmlFor='HWSet'>Hardware Set</label>
<select
	name='HWSet'>
	<option value="HWSet1">HWSet 1</option>
	<option value="HWSet2">HWSet 2</option>
	value={this.state.HWSet}
	onChange={this.handleChange}
</select>   */}