import React from "react";
import { getWorkouts } from "../services/workoutService";
import { useState, useEffect } from "react";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    async function getData() {
      setWorkouts(await getWorkouts());
    }
    getData();
  });

  return (
    <>
      <Card>
        <Card.Header>Featured</Card.Header>
        <Card.Body>
          <Card.Title>Special title treatment</Card.Title>
          <Card.Text>
            With supporting text below as a natural lead-in to additional
            content.
          </Card.Text>
          <Button variant="primary">Go somewhere</Button>
        </Card.Body>
      </Card>
      <div className="card">{workouts.map((workout) => workout.title)}</div>
    </>
  );
};

export default Workouts;
