import React, { Fragment } from "react";
import { useDrop } from "react-dnd";
import Workout from "./Workout";
import Card from "react-bootstrap/Card";
import zoneStyle from "../utils/zoneStyle";
import dayOfWeek from "../utils/dayOfWeek";
import { ItemTypes } from "../utils/Constants";

function WorkoutCardContainer({ id, date, workouts }) {
  const [{ isOver }, drop] = useDrop({
    accept: ItemTypes.WORKOUT,
    drop: (props) => console.log(props.title + " got dropped into " + id),
    collect: (monitor) => ({
      isOver: !!monitor.isOver(),
    }),
  });

  return (
    <Fragment key={id + "fragment"}>
      <Card
        ref={drop}
        key={id}
        className="text-bold"
        text="dark"
        variant="top"
        border="dark"
        bg={isOver ? "light" : ""}
      >
        <Card.Header as="h5" key={id + "header"} className="text-center mb-1">
          <p>{dayOfWeek(date)}</p>
          <p>{date}</p>
        </Card.Header>
        {workouts.map(({ id, zone, title }) => (
          <Workout key={id} id={id} zone={zoneStyle(zone)} title={title} />
        ))}
      </Card>
    </Fragment>
  );
}

export default WorkoutCardContainer;
