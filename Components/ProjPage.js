import React, { useState, Component } from "react";
import './components.css';
import { Navigate, useNavigate } from "react-router-dom";

import HWManagement from "./HWManagement";



function ProjPage() {

  const navigate = useNavigate()
 
       
      
    function NewProjectClick(){
     

    navigate("/hwManagement")
    }

    
    
    function OpenExistingClick(){

     
      navigate("/hwManagement")
    }
     
      
   
    return (
     
       
      <div className='app2'>
          <div>
          <form>
          <label>Create New Project </label>
          <div className="input-container">
            <label>Project Name </label>
            <input type="text" name="pname" id = "pname" required  />
            
          </div>
          <div className="input-container">
            <label>Project Description </label>
            <input type="text" name="pdescrip" id = "pdescrip" required />
            
          </div>
          <div className="input-container">
            <label>Funds </label>
            <input type="text" name="funds" id = "funds" required />
            
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
            <input type="text" name="epname" id = "epname" required />
            
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