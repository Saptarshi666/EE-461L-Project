import React, { useState, Component } from "react";
import './index.css';




function NewProj({ isShowNew, handleProjClick}) {

       
      
    function NewProjectClick(){

      handleProjClick();

    }
    
    function OpenExistingClick(){

      handleProjClick();

    }
     
      
   
    return (
        <div className={`${isShowNew ? "active" : ""} show`}>
          <div>
          <span onClick={NewProjectClick} className="btn">
              New Project
          </span>
          <span onClick={OpenExistingClick} className="btn">
              Open Existing Project
          </span>
          </div>
              
      </div>
    );
    
}
  
  export default NewProj;