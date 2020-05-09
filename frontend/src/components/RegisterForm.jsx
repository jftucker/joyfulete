import React from "react";
import Joi from "joi-browser";
import Form from "./common/Form";
import { toast } from "react-toastify";
import auth from "../services/authService";

class RegisterForm extends Form {
  state = {
    data: {
      email: "",
      password: "",
      username: "",
    },
    errors: {},
  };

  schema = {
    email: Joi.string().required().email().label("Email"),
    password: Joi.string().required().min(5).label("Password"),
    username: Joi.string().required().label("Name"),
  };

  doLogin = async ({ data }) => {
    const response = await auth.login(data.email, data.password);
    if (response.status === 401) {
      toast.error(response.data.detail);
      return;
    }
    window.location = "/";
  };

  doSubmit = async () => {
    try {
      const response = await auth.register(this.state.data);
      if (response.status === 400) {
        this.setState({ errors: response.data });
        return;
      }
      this.doLogin(this.state);
    } catch (ex) {}
  };

  render() {
    return (
      <div>
        <h1>Register</h1>
        <form onSubmit={this.handleSubmit}>
          {this.renderInput("email", "Email")}
          {this.renderInput("password", "Password", "password")}
          {this.renderInput("username", "Username")}
          {this.renderButton("Register")}
        </form>
      </div>
    );
  }
}

export default RegisterForm;
