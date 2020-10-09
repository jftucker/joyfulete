import React, { Fragment } from "react";
import { useDrop } from "react-dnd";
import Workout from "./Workout";
import Card from "react-bootstrap/Card";
import zoneStyle from "../utils/zoneStyle";
import dayOfWeek from "../utils/dayOfWeek";
import { moveWorkout } from "../utils/workouts";
import { ItemTypes } from "../utils/Constants";
import _ from "lodash";

function WorkoutCardContainer(props) {
  const onDrop = droppedProps => {
    const toDay = _.find(props.week.days, obj => obj.id === props.id);
    const fromDay = _.find(
      props.week.days,
      obj => obj.id === droppedProps.dayId
    );
    if (droppedProps.dayId !== props.id && fromDay)
      moveWorkout(fromDay, toDay, props, droppedProps);

    console.log(droppedProps);
  };

  const [{ isOver }, drop] = useDrop({
    accept: ItemTypes.WORKOUT,
    drop: onDrop,
    collect: monitor => ({
      isOver: monitor.isOver(),
    }),
  });

  return (
    <Fragment key={props.id + "fragment"}>
      <Card
        ref={drop}
        key={props.id}
        className='text-bold mb-3'
        text='dark'
        variant='top'
        border='dark'
        bg={isOver ? "light" : ""}
      >
        <Card.Header
          as='h5'
          key={props.id + "header"}
          className='text-center mb-1'
        >
          <p>{dayOfWeek(props.date)}</p>
          <p>{props.date}</p>
        </Card.Header>
        {props.workouts.map(({ id: workoutId, zone, title }) => (
          <Workout
            key={workoutId}
            id={workoutId}
            zone={zoneStyle(zone)}
            title={title}
            dayId={props.id}
          />
        ))}
      </Card>
    </Fragment>
  );
}

export default WorkoutCardContainer;
