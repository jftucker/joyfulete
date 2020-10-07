import React, { Fragment } from "react";
import { useDrop } from "react-dnd";
import Workout from "./Workout";
import Card from "react-bootstrap/Card";
import zoneStyle from "../utils/zoneStyle";
import dayOfWeek from "../utils/dayOfWeek";
import { ItemTypes } from "../utils/Constants";
import _ from "lodash";

function WorkoutCardContainer({ id, date, workouts, week, setWeek }) {
  const onDrop = props => {
    const newWeek = { ...week };
    const toDay = _.find(newWeek.days, obj => obj.id === id);
    const fromDay = _.find(newWeek.days, obj => obj.id === props.dayId);

    console.log(week);

    if (props.dayId !== id && fromDay) {
      const newDays = newWeek.days.filter(
        item => item.id !== props.dayId && item.id !== id
      );
      const workout = _.find(fromDay.workouts, obj => obj.id === props.id);

      fromDay.workouts = fromDay.workouts.filter(
        workout => workout.id !== props.id
      );
      toDay.workouts = [...toDay.workouts, workout];

      newWeek.days = [...newDays, toDay, fromDay].sort((a, b) =>
        a.date > b.date ? 1 : -1
      );

      setWeek(newWeek);
    }
  };
  const [{ isOver }, drop] = useDrop({
    accept: ItemTypes.WORKOUT,
    drop: onDrop,
    collect: monitor => ({
      isOver: monitor.isOver(),
    }),
  });

  return (
    <Fragment key={id + "fragment"}>
      <Card
        ref={drop}
        key={id}
        className='text-bold mb-3'
        text='dark'
        variant='top'
        border='dark'
        bg={isOver ? "light" : ""}
      >
        <Card.Header as='h5' key={id + "header"} className='text-center mb-1'>
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
