import React, { useState, Component } from "react";
import './index.css';
import { useNavigate, Link } from "react-router-dom";




function NewProj({ isShowNew, handleProjClick}) {
      
    function NewProjectClick(){
      handleProjClick()
      const navigate = useNavigate()
      let path = '/ProjPage'; 
      navigate(path);

    
    }

    return (
     
        <div className={`${isShowNew ? "active" : ""} show`}>
          <div>
            
          <span onClick={NewProjectClick} className="btn">
              Go To Project Page
          </span>
          
          </div>
              
      </div>
     
    );
    
}
  
  export default NewProj;