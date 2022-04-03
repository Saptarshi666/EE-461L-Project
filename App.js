import "./index.css";
import React, { useState } from "react";
import PopUp from "./PopUp";
import LoginScreen from "./LoginScreen";
import NewProj from "./NewProj"



export default function App() {

  const [isShowLogin, setIsShowLogin] = useState(true);
  const [isShowOrig, setIsShowOrig] = useState(false);
  const [isShowNew, setIsShowNew] = useState(true);

  
    
   
 
    
    

  const handleUserClick = () => {
    setIsShowLogin(false);
    setIsShowOrig(true);
    
    
      };
  
  const handleProjClick = () => {
    setIsShowLogin(true);
    setIsShowOrig(true);
    setIsShowNew(false)
        
        
          };

  

  return (
    
     <div className="app">
      
      <LoginScreen isShowOrig= {isShowOrig} handleUserClick={handleUserClick} handleProjClick = {handleProjClick} />
      <PopUp isShowLogin={isShowLogin} handleProjClick = {handleProjClick}/>
      <NewProj isShowNew={isShowNew} handleProjClick = {handleProjClick} />
           
      
    
    </div>
  );
}

