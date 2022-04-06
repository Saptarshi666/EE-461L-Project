import "./index.css";
import React, { useState } from "react";
import PopUp from "./PopUp";
import LoginScreen from "./LoginScreen";
import NewProj from "./NewProj"
import ProjPage from "./ProjPage"
import ExistingProjects from "./ExistingProjects"



export default function App() {

  const [isShowLogin, setIsShowLogin] = useState(true);
  const [isShowOrig, setIsShowOrig] = useState(false);
  const [isShowNew, setIsShowNew] = useState(true);
  const [isShowProjPage, setIsShowProjPage] = useState(true);

  
    
   
 
    
    

  const handleUserClick = () => {
    setIsShowLogin(false);
    setIsShowOrig(true);
    
    
      };
  
  const handleProjClick = () => {
    setIsShowNew(true);
    setIsShowProjPage(false);
    
        
        
          };
  const handleSubmitClick = () => {
    setIsShowLogin(true);
    setIsShowOrig(true);
    setIsShowNew(false);
    
            
                
                
                  };

 
  

  return (
    
     
       <div className = "show">
          <div className = "app">
      
      <LoginScreen isShowOrig= {isShowOrig} handleUserClick={handleUserClick} handleSubmitClick = {handleSubmitClick} />
      <PopUp isShowLogin={isShowLogin} handleSubmitClick = {handleSubmitClick}/>
      </div>
      <div className = "app2">
      <NewProj isShowNew={isShowNew} handleProjClick = {handleProjClick} />
      <ProjPage isShowProjPage={isShowProjPage} />   
     
      <ExistingProjects isShowProjPage={isShowProjPage} />  
      
      </div>
      </div>
    
   
  );
}

