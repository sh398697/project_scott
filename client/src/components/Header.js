import React, { useContext, useEffect, useState } from "react";
import { NavLink } from "react-router-dom";
import "./Header.css";

function Header() {

    return (
        <div>
            <div className="header-container">
                <ul className="header-menu">
                    <li><NavLink to="/">Home</NavLink></li>
                    <li><NavLink to="/users">Users</NavLink></li>
                    <li><NavLink to="/posts">Posts</NavLink></li>
                </ul>
            </div>
        </div>
  );
}

export default Header;
