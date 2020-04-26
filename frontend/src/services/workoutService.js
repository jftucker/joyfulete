import http from "./httpService";
import { apiUrl } from "../config.json";

const apiEndpoint = apiUrl + "/workouts";

function workoutUrl(id) {
  return `${apiEndpoint}/${id}`;
}

export function getWorkouts() {
  return http.get(apiEndpoint);
}

export function getWorkout(workoutId) {
  return http.get(workoutUrl(workoutId));
}

export function saveWorkout(workout) {
  if (workout._id) {
    const body = { ...workout };
    delete body._id;
    return http.put(workoutUrl(workout._id), body);
  }

  return http.post(apiEndpoint, workout);
}

export function deleteWorkout(workoutId) {
  return http.delete(workoutUrl(workoutId));
}
