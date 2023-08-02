import React, { useState, useEffect } from "react";
import {BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import API_URL from "./apiConfig";
import Header from "./components/Header";
import Home from "./components/Home";
import Users from "./components/Users";
import Posts from "./components/Posts";
import './App.css';

function App() {

  const [users, setUsers] = useState([]);
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/users`)
        .then((r) => r.json())
        .then(setUsers);
  }, []);

  useEffect(() => {
    fetch(`${API_URL}/posts`)
        .then((r) => r.json())
        .then(setPosts);
  }, []);

  return (
    <div className="App">
      <Router>
        <Header />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/users" element={<Users users={users} setUsers={setUsers} />} />
          <Route path="/posts" element={<Posts posts={posts} setPosts={setPosts} />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
