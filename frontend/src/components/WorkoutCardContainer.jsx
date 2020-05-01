import React, { Fragment } from "react";
import { useDrop } from "react-dnd";
import Workout from "./Workout";
import Card from "react-bootstrap/Card";
import zoneStyle from "../utils/zoneStyle";
import dayOfWeek from "../utils/dayOfWeek";
import { ItemTypes } from "../utils/Constants";

function WorkoutCardContainer({ id, date, workouts, week, setWeek }) {
  const onDrop = (props) => {
    if (props.dayId !== id) {
      const newWeek = { ...week };
      const toDay = newWeek.days.filter((item) => item.id === id);
      const fromDay = newWeek.days.filter((item) => item.id === props.dayId);
      const newDays = newWeek.days.filter(
        (item) => item.id !== props.dayId && item.id !== id
      );
      const workout = fromDay[0].workouts.filter(
        (workout) => workout.id === props.id
      )[0];
      fromDay[0].workouts = fromDay[0].workouts.filter(
        (workout) => workout.id !== props.id
      );
      toDay[0].workouts = [...toDay[0].workouts, workout];

      newWeek.days = [...newDays, toDay[0], fromDay[0]].sort((a, b) =>
        a.date > b.date ? 1 : -1
      );

      setWeek(newWeek);
    }
  };
  const [{ isOver }, drop] = useDrop({
    accept: ItemTypes.WORKOUT,
    drop: onDrop,
    collect: (monitor) => ({
      isOver: !!monitor.isOver(),
    }),
  });

  return (
    <Fragment key={id + "fragment"}>
      <Card
        ref={drop}
        key={id}
        className="text-bold mb-3"
        text="dark"
        variant="top"
        border="dark"
        bg={isOver ? "light" : ""}
      >
        <Card.Header as="h5" key={id + "header"} className="text-center mb-1">
          <p>{dayOfWeek(date)}</p>
          <p>{date}</p>
        </Card.Header>
        {workouts.map(({ id: workoutId, zone, title }) => (
          <Workout
            key={workoutId}
            id={workoutId}
            zone={zoneStyle(zone)}
            title={title}
            dayId={id}
          />
        ))}
      </Card>
    </Fragment>
  );
}

export default WorkoutCardContainer;
