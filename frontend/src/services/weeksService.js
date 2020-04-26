import http from "./httpService";
import { apiUrl } from "../config.json";

const apiEndpoint = apiUrl + "/plans/weeks";

function weekUrl(id) {
  return `${apiEndpoint}/${id}`;
}

export function getWeeks() {
  return http.get(apiEndpoint);
}

export function getWeek(weekId) {
  return http.get(weekUrl(weekId));
}

export function saveWeek(week) {
  if (week._id) {
    const body = { ...week };
    delete body._id;
    return http.put(weekUrl(week._id), body);
  }

  return http.post(apiEndpoint, week);
}

export function deleteWeek(weekId) {
  return http.delete(weekUrl(weekId));
}
