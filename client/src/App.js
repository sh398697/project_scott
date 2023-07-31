import React, { useState, useEffect } from "react";
import {BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import API_URL from "./apiConfig";
import Home from "./components/Home";
import './App.css';

function App() {

  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/users`)
        .then((r) => r.json())
        .then(setUsers);
}, []);

  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Home users={users} setUsers={setUsers} />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
