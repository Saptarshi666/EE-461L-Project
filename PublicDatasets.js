import React,{ Component } from 'react'
import "./index.css";

class PublicDatasets extends Component{
constructor(props){
	super(props)
}

// Form submitting logic


// Method causes to store all the values of the
// input field in react state single method handle


// Return a controlled form i.e. values of the
// input field not stored in DOM values are exist
// in react component itself as state
render(){
	return(
    <ul>
      <li onClick={this.handleCheck}>Abdominal and Direct Fetal ECG Database</li>
      <li onClick={this.handleCheck}>AF Termination Challenge Database</li>
      <li onClick={this.handleCheck}>AHA Database Sample Excluded Record</li>
      <li onClick={this.handleCheck}>A multi-camera and multimodal dataset for posture and gait analysis</li>
      <li onClick={this.handleCheck}>ANSI/AAMI EC13 Test Waveforms</li>
    </ul> 	
    )
}

}
export default PublicDatasets

