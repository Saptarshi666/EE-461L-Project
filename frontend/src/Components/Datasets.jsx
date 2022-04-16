import React from 'react'
import axios from 'axios'

const dataset = [
  {name : "Adominal and Direct Fetal ECGb Database", id: '1'}, 
  {name : "AF Termination Challenge Database", id: '2'}, 
  {name : "AHA Database Sample Excluded Record", id: '3'}, 
  {name : "ANSI/AAMI EC13 Test Waveforms", id: '4'},
  {name : "Apnea-ECG Database:", id: '5'}, 
];

const Datasets = () => (
  <List list={dataset} />
);

function Download(props){
  axios({
        url: `./public/files/${this.props.file}`,
        method: "GET",
        headers: 'default',
        responseType: "blob" // important
    }).then(response => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute(
            "download",
            `${this.props.file.name}.${this.props.file.mime}`
        );
        document.body.appendChild(link);
        link.click();

        // Clean up and remove the link
        link.parentNode.removeChild(link);
    });
}

function log(url) {
  console.log(url);
}



function ListItem(props) {
  // --> displays the data 
  return <li onClick={() => log(props.value)}>
            <div>{props.value.name}</div>
            <div>{ "  Author Name: " + props.value.id}</div>
            <div>{ "  Date Created: " + props.value.id}</div>
            <div>{ "  File Size: " + props.value.id}</div>
            <div>{ ""}</div>


        </li>;
}

function List() {

  const listItems = dataset.map((item) =>
    <ListItem key={item.name} value={item} />
  );

  return (
    <ul>
      {listItems}
    </ul>
  );
}



export default Datasets