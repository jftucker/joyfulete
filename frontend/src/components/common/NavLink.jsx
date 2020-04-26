import React from "react";
import { LinkContainer } from "react-router-bootstrap";
import Nav from "react-bootstrap/Nav";
const NavLink = ({ to, children }) => {
  return (
    <LinkContainer to={to}>
      <Nav.Link href={to}>{children}</Nav.Link>
    </LinkContainer>
  );
};

export default NavLink;
