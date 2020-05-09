import React, { useState, useEffect } from "react";
import { Route, Redirect, Switch } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import Home from "./components/Home";
import LoginForm from "./components/LoginForm";
import Logout from "./components/Logout";
import NotFound from "./components/NotFound";
import NavBar from "./components/NavBar";
import Plan from "./components/Plan";
import RegisterForm from "./components/RegisterForm";
import Weeks from "./components/Weeks";
import auth from "./services/authService";
import "react-toastify/dist/ReactToastify.css";
import "./App.css";

function App() {
  const [user, setUser] = useState({});

  useEffect(() => {
    setUser(auth.getCurrentUser());
  }, []);

  return (
    <React.Fragment>
      <ToastContainer />
      <NavBar user={user} />
      <main className="container">
        <Switch>
          <Route path="/home" component={Home} />
          <Route path="/plan" component={Plan} />
          <Route path="/weeks" component={Weeks} />
          <Route path="/register" component={RegisterForm} />
          <Route path="/login" component={LoginForm} />
          <Route path="/logout" component={Logout} />
          <Route path="/not-found" component={NotFound} />
          <Redirect from="/" exact to="/home" />
          <Redirect to="/not-found" />
        </Switch>
      </main>
    </React.Fragment>
  );
}

export default App;
