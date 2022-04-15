import React, { useState, Component } from "react";
import './components.css';
import { useNavigate } from "react-router-dom";




function ProjPage() {
  const navigate = useNavigate()
  const [projName, setprojname] = useState("");
  const [projDesc, setprojdesc] = useState("");
  const [projID, setprojid] = useState("");
  const [result, setresult] = useState("");

    function NewProjectClick(){
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ projName: projName , projDesc: projDesc, projID: projID})
      };
      fetch("/projectpage", requestOptions)
      .then(response => response.json())
      .then(data => this.setState(data.result));
      // this.setState({email: val.currentTarget.value})
      console.log(result)
      navigate("/HWManagement/")       
    }

    
    
    function OpenExistingClick(){
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({projID: projID})
      };
      fetch("/projectpage1", requestOptions)
      .then(response => response.json())
      .then(data => console.log(data.result));
      // this.setState({email: val.currentTarget.value})
      console.log(result)
      navigate("/HWManagement")       
    }
     
      
   
    return (
     
       
      <div className='app2'>
          <div>
          <form>
          <label>Create New Project </label>
          <div className="input-container">
            <label>Project Name </label>
            <input type="text" name="pname" value={projName} id = "pname" required onChange = {(e) => setprojname(e.target.value)} />
            
          </div>
          <div className="input-container">
            <label>Project Description </label>
            <input type="text" name="pdescrip" value={projDesc} id = "pdescrip" required onChange = {(e) => setprojdesc(e.target.value)} />
            
          </div>
          <div className="input-container">
            <label>Project ID </label>
            <input type="text" name="projID" value={projID} id = "projID" required onChange = {(e) => setprojid(e.target.value)} />
            
          </div>
          <div className="button-container">
          <span onClick={NewProjectClick} className="btn">
              Create New Project
          </span>
          </div>
          </form>
          </div>
         
         <div></div>
         
         <div >
           <form>
         <label>Open Existing Project </label>
          <div className="input-container">
            <label>ProjectID </label>
            <input type="text" name="epname" value={projID} id = "epname" required onChange = {(e) => setprojid(e.target.value)}/>
            
          </div>
          <div className="button-container">
          <span onClick={OpenExistingClick} className="btn">
              Open Existing Project
          </span>
          </div>
          </form>
          </div>    
      </div>
     
    );
    
}
  
  export default ProjPage;