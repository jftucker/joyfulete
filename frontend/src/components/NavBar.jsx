import React from "react";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import NavLink from "./common/NavLink";

const NavBar = () => {
  return (
    <Navbar collapseOnSelect expand="lg" bg="light" className="mb-2">
      <Navbar.Brand href="/">Joyfulete</Navbar.Brand>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
      <Navbar.Collapse id="responsive-navbar-nav">
        <Nav className="mr-auto">
          <NavLink to="/home">Home</NavLink>
          <NavLink to="/plan">Plan</NavLink>
          <NavLink to="/weeks">Weeks</NavLink>
          <NavLink to="/fitness">Fitness</NavLink>
          <NavLink to="/calendar">Calendar</NavLink>
        </Nav>
        <Nav>
          <NavLink to="/login">Login</NavLink>
          <NavLink to="/register">Register</NavLink>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default NavBar;
