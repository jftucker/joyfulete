import React from "react";
import Joi from "joi-browser";
import Form from "./common/Form";
import * as userService from "../services/userService";

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

  doSubmit = async () => {
    try {
      const response = await userService.register(this.state.data);
      if (response.status === 400) {
        // const errors = { ...response.data };
        this.setState({ errors: response.data });
      }
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
