import React from "react";
import Joi from "joi-browser";
import { toast } from "react-toastify";
import Form from "./common/Form";
import auth from "../services/authService";

class LoginForm extends Form {
  state = {
    data: { email: "", password: "" },
    errors: {},
  };

  schema = {
    email: Joi.string().required().label("Username"),
    password: Joi.string().required().min(5).label("Password"),
  };

  doSubmit = async () => {
    try {
      const { data } = this.state;
      const response = await auth.login(data.email, data.password);
      if (response.status === 401) {
        toast.error(response.data.detail);
        return;
      }
      window.location = "/";
    } catch (ex) {}
  };

  render() {
    return (
      <div>
        <h1>Login</h1>
        <form onSubmit={this.handleSubmit}>
          {this.renderInput("email", "Email")}
          {this.renderInput("password", "Password", "password")}
          {this.renderButton("Login")}
        </form>
      </div>
    );
  }
}

export default LoginForm;
