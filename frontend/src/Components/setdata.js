import React, { useState, Component } from "react";
import './components.css';
import { useNavigate } from "react-router-dom";




function SetsDatas() {
  const navigate = useNavigate()
  const [setabbrev, setdsabbrev] = useState("");
  const [title, settitle] = useState("");
  const [desc, setdesc] = useState("");
  const [zipfile, setzipfile] = useState("");
  const [result, setresult] = useState("");
  const [title2, settitle2] = useState("");
  const [desc2, setdesc2] = useState("");
  const [zipfile2, setzipfile2] = useState("");
  const [result2, setresult2] = useState("");
  const [title3, settitle3] = useState("");
  const [desc3, setdesc3] = useState("");
  const [zipfile3, setzipfile3] = useState("");
  const [result3, setresult3] = useState("");
  const [title4, settitle4] = useState("");
  const [desc4, setdesc4] = useState("");
  const [zipfile4, setzipfile4] = useState("");
  const [result4, setresult4] = useState("");
  const [title5, settitle5] = useState("");
  const [desc5, setdesc5] = useState("");
  const [zipfile5, setzipfile5] = useState("");
  const [result5, setresult5] = useState("");
  
    function GetZipfile1(){
      const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ '_id': 'aami-ec13'})
      };
      fetch("/zipfile", requestOptions)
      .then(response => response.json())
      .then(data => setresult(data));
      // this.setState({email: val.currentTarget.value})
      console.log(result)  
      settitle(result["title"])
      setdesc(result["desc"])
      setzipfile(result["result"])
      console.log(title)
    }
    function GetZipfile2(){
        const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ '_id': 'bpssrat'})
        };
        fetch("/zipfile", requestOptions)
        .then(response => response.json())
        .then(data => setresult2(data));
        // this.setState({email: val.currentTarget.value})
        console.log(result2)  
        settitle2(result2["title"])
        setdesc2(result2["desc"])
        setzipfile2(result2["result"])
        console.log(title)
      }
      function GetZipfile3(){
        const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ '_id': 'adfecgdb'})
        };
        fetch("/zipfile", requestOptions)
        .then(response => response.json())
        .then(data => setresult3(data));
        // this.setState({email: val.currentTarget.value})
        console.log(result3)  
        settitle3(result3["title"])
        setdesc3(result3["desc"])
        setzipfile3(result3["result"])
        console.log(title3)
      }
      function GetZipfile4(){
        const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ '_id': 'aftdb'})
        };
        fetch("/zipfile", requestOptions)
        .then(response => response.json())
        .then(data => setresult4(data));
        // this.setState({email: val.currentTarget.value})
        console.log(result4)  
        settitle4(result4["title"])
        setdesc4(result4["desc"])
        setzipfile4(result4["result"])
        console.log(title4)
      }
      function GetZipfile5(){
        const requestOptions = {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ '_id': 'norwegian-athlete-ecg'})
        };
        fetch("/zipfile", requestOptions)
        .then(response => response.json())
        .then(data => setresult5(data));
        // this.setState({email: val.currentTarget.value})
        console.log(result5)  
        settitle5(result5["title"])
        setdesc5(result5["desc"])
        setzipfile5(result5["result"])
        console.log(title5)
      }
   
    return (
     
       
      <div className='app3'>
          <div>
          <form>
		  	<h2>Title: {title} </h2>
			  <label>Description: {desc}</label>
			  <span onClick={GetZipfile1} className="btn">
              Load Set</span>
              <a href={zipfile}>Download the ZIP file</a>
            <label>{"\n"}</label>
		  	<h2>Title: {title2} </h2>
			  <label>Description: {desc2}</label>
			  <span onClick={GetZipfile2} className="btn">
              Load Set</span>
              <a href={zipfile2}>Download the ZIP file</a>
		  	<h2>Title: {title3} </h2>
			  <label>Description: {desc3}</label>
			  <span onClick={GetZipfile3} className="btn">
              Load Set</span>
              <a href={zipfile3}>Download the ZIP file</a>
		  	<h2>Title: {title4} </h2>
			  <label>Description: {desc4}</label>
			  <span onClick={GetZipfile4} className="btn">
              Load Set</span>
              <a href={zipfile4}>Download the ZIP file</a>
		  	<h2>Title: {title5} </h2>
			  <label>Description: {desc5}</label>
			  <span onClick={GetZipfile5} className="btn">
              Load Set</span>
              <a href={zipfile5}>Download the ZIP file</a>
          </form>
          </div>
         
         <div></div>
         
         <div >
           <form>

          </form>
          </div>    
      </div>
     
    );
    
}
  
  export default SetsDatas;