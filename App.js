import "./index.css";
import React, { useState } from "react";
import PopUp from "./PopUp";
import LoginScreen from "./LoginScreen";



export default function App() {

  const [isShowLogin, setIsShowLogin] = useState(true);
  const [isShowOrig, setIsShowOrig] = useState(false);
    
   
 
   const handleSubmitClick=() =>{
    setIsShowOrig(true);
    setIsShowLogin(true);
    
       
    
   };

  
    

  const handleUserClick = () => {
    setIsShowLogin(false);
    setIsShowOrig(true);
    
    
      };

  

  return (
    
     <div className="app">
      <div className="login-form">
        <div className="title">Sign In</div>
      <LoginScreen isShowOrig= {isShowOrig} handleUserClick={handleUserClick} handleSubmitClick = {handleSubmitClick} />
      <PopUp isShowLogin={isShowLogin} handleSubmitClick = {handleSubmitClick} />
           
      
    </div>
    </div>
  );
}

