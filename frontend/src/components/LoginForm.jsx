import React from "react";
import Joi from "joi-browser";
import { toast } from "react-toastify";
import Form from "./common/Form";
import * as userService from "../services/userService";

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
      const response = await userService.login(data.email, data.password);
      if (response.status === 400) {
        response.data.non_field_errors.map((item) => toast.error(item));
      }
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
