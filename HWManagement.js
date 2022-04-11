import React,{ Component } from 'react'
import "./index.css";

class HWManagement extends Component{
constructor(props){
	super(props)
	this.state = { project:'',HWSet:'', action:'',units:''}
	this.handleChange = this.handleChange.bind(this)
	this.handleSubmit = this.handleSubmit.bind(this)
}

// Form submitting logic
handleSubmit(event){
	const { project, HWSet, action, units} = this.state
	event.preventDefault()
	alert(`
	____Your Details____\n
	Project : ${project}
	HWSet : ${HWSet}
	Action : ${action}
	Value : ${units}
	`)
}

// Method causes to store all the values of the
// input field in react state single method handle
handleChange(event){
	this.setState({
	[event.target.project] : event.target.value
	})
}

// Return a controlled form i.e. values of the
// input field not stored in DOM values are exist
// in react component itself as state
render(){
	return(
	<form onSubmit={this.handleSubmit}>
		<div>
		</div>
		<div>
		<label htmlFor='project'>Project</label>
		<select
			name='Project'>
            <option value="proj1">Project1</option>
            <option value="proj2">Project2</option>
            value={this.state.project}
			onChange={this.handleChange}
        </select>  
		</div>
		<div>
		<label htmlFor='HWSet'>Hardware Set</label>
		<select
			name='HWSet'>
            <option value="HWSet1">HWSet 1</option>
            <option value="HWSet2">HWSet 2</option>
            value={this.state.HWSet}
			onChange={this.handleChange}
        </select>  
		</div>
		<div>
		<label htmlFor='action'>Action</label>
		<select
			name='Action'>
            <option value="checkin">Check In</option>
            <option value="checkout">Check Out</option>
            value={this.state.action}
			onChange={this.handleChange}
        </select>  
		</div>
        <div>
		<label htmlFor='units'>Units</label>
		<input
			name='Units'
			placeholder='0'
			value={this.state.units}
			onChange={this.handleChange}
		/>
		</div>
		<div>
		<button> Submit </button>
		</div>
	</form>
	)
}
}

export default HWManagement

