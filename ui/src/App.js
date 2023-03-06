import React, { useState, useEffect } from "react";
import logo from './logo.svg';
import './App.css';

function App() {

  const payload = {
        message: "",
        company:"",
        location:"",
        year:0,
        month:"",
        Country:"",
        Project:"",
        supervisor:"",
  }

  const [data, setdata] = useState(payload);

  useEffect(() => { fetch("/").then(res => res.json()).then(data => setdata({
        message: data.message,
        company:data.company,
        location:data.location,
        year:data.year,
        month:data.month,
        Country:data.Country,
        Project:data.Project,
        supervisor:data.supervisor,
  }));
  }, []);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>{data.message}</p>
        <p>{data.company}</p>
        <p>{data.location}</p>
        <p>{data.year}</p>
        <p>{data.month}</p>
        <p>{data.Country}</p>
        <p>{data.Project}</p>
        <p>{data.supervisor}</p>
    
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
