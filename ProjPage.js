import React, { useState, Component } from "react";
import './index.css';
import { useNavigate } from "react-router-dom";




function ProjPage({ isShowProjPage, handleProjClick}) {

 
 
       
      
    function NewProjectClick(){
     

    
    }

    
    
    function OpenExistingClick(){

     

    }
     
      
   
    return (
     
       
      <div className={`${isShowProjPage ? "active" : ""} show`}>
          <div>
          <span onClick={NewProjectClick} className="btn">
              New Project
          </span>
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
          </div>
         
         
              
      </div>
     
    );
    
}
  
  export default ProjPage;