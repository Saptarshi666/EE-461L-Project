import React, { useState, Component } from "react";
import './components.css';
import { useNavigate, Link } from "react-router-dom";

export default function ProjDetails(){

  const [ID, setID] = useState("");
  const [Description, setDescription] = useState("");
  const [Funds, setFunds] = useState("");

    return (
        <div className= 'app'>
            <form>
            <div className="text">
              <label>ProjectID </label>
              
            
          </div>
          <div className="text">
            <label>Description </label>
           
            
          </div>
          <div className="text">
          <label>Funds </label>
         
            </div>
          </form>      
        </div>
      );
}
