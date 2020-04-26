import React from "react";
import { Route, Redirect, Switch } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import Calendar from "./components/Calendar";
import Fitness from "./components/Fitness";
import Home from "./components/Home";
import LoginForm from "./components/LoginForm";
import NotFound from "./components/NotFound";
import NavBar from "./components/NavBar";
import Plan from "./components/Plan";
import RegisterForm from "./components/RegisterForm";
import Workouts from "./components/Workouts";
import "react-toastify/dist/ReactToastify.css";
import "./App.css";
import Weeks from "./components/Weeks";

function App() {
  return (
    <React.Fragment>
      <ToastContainer />
      <NavBar />
      <main className="container">
        <Switch>
          <Route path="/home" component={Home} />
          <Route path="/plan" component={Plan} />
          <Route path="/weeks" component={Weeks} />
          <Route path="/workouts" component={Workouts} />
          <Route path="/fitness" component={Fitness} />
          <Route path="/calendar" component={Calendar} />
          <Route path="/register" component={RegisterForm} />
          <Route path="/login" component={LoginForm} />
          <Route path="/not-found" component={NotFound} />
          <Redirect from="/" exact to="/home" />
          <Redirect to="/not-found" />
        </Switch>
      </main>
    </React.Fragment>
  );
}

export default App;
