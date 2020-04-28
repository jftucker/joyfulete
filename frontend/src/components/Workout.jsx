import React from "react";
import { ItemTypes } from "../utils/Constants";
import { useDrag } from "react-dnd";
import Card from "react-bootstrap/Card";

function Workout({ id, zone, title }) {
  const [{ isDragging }, drag] = useDrag({
    item: { type: ItemTypes.WORKOUT, id: id, zone: zone, title: title },
    collect: (monitor) => ({
      isDragging: !!monitor.isDragging(),
    }),
  });

  return (
    <Card
      key={id}
      ref={drag}
      style={{
        opacity: isDragging ? 0.5 : 1,
        cursor: "move",
      }}
      text={zone}
      border={zone}
      className="mb-1 mx-1 p-1"
    >
      <Card.Title key={id + "title"} className="my-auto text-center" as="h6">
        {title}
      </Card.Title>
    </Card>
  );
}

export default Workout;
