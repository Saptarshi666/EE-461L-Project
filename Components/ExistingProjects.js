import React, { useState, Component } from "react";
import './index.css';
import { useNavigate } from "react-router-dom";




function ExistingProjects({ isShowProjPage}) {

 
 
       
      
    function NewProjectClick(){
     

    
    }

    
    
   
     
      
   
    return (
     
       
      <div className={`${isShowProjPage ? "active" : ""} show`}>
          
          <div className= "title">
          Existing Projects
          </div>
         
              
      </div>
     
    );
    
}
  
  export default ExistingProjects;