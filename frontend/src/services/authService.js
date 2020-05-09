import jwtDecode from "jwt-decode";
import http from "./httpService";
import { apiUrl } from "../config.json";

const ACCESS_TOKEN_KEY = "access";
const REFRESH_TOKEN_KEY = "refresh";

export async function register(user) {
  const response = await http
    .post(apiUrl + "/rest-auth/registration/", {
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

export async function login(username, password) {
  const response = await http
    .post(apiUrl + "/token/", { username, password })
    .then((response) => {
      localStorage.setItem(ACCESS_TOKEN_KEY, response.data.access);
      localStorage.setItem(REFRESH_TOKEN_KEY, response.data.refresh);
      return response;
    })
    .catch((error) => {
      return error.response;
    });
  return response;
}

export function logout() {
  localStorage.removeItem(ACCESS_TOKEN_KEY);
  localStorage.removeItem(REFRESH_TOKEN_KEY);
}

export function getCurrentUser() {
  try {
    const accessToken = localStorage.getItem(ACCESS_TOKEN_KEY);
    return jwtDecode(accessToken);
  } catch (error) {
    return null;
  }
}

export default {
  getCurrentUser,
  login,
  logout,
  register,
};
