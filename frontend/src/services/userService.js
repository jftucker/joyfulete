import http from "./httpService";
import { apiUrl } from "../config.json";

const apiEndpoint = apiUrl + "/rest-auth/";

export function register(user) {
  const response = http
    .post(apiEndpoint + "registration/", {
      username: user.username,
      email: user.email,
      password1: user.password,
      password2: user.password,
    })
    .then((response) => {
      return response;
    })
    .catch((error) => {
      return error.response;
    });
  return response;
}

export function login(email, password) {
  const response = http
    .post(apiEndpoint + "login/", { email, password })
    .then((response) => {
      return response;
    })
    .catch((error) => {
      return error.response;
    });
  return response;
}
