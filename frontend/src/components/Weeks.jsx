import React from "react";
import { getWeek } from "../services/weeksService";
import { useState, useEffect } from "react";
import { DndProvider } from "react-dnd";
import Backend from "react-dnd-html5-backend";
import CardGroup from "react-bootstrap/CardGroup";
import WorkoutCardContainer from "./WorkoutCardContainer";

const Week = () => {
  const [week, setWeek] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const result = await getWeek("7b8f7eb2-1742-450d-a2f0-40b8122e6f51");
      setWeek(result.data);
    };

    fetchData();
  }, []);

  return (
    <DndProvider backend={Backend}>
      <CardGroup>
        {week.days
          ? week.days.map(({ id, date, workouts }) => (
              <WorkoutCardContainer
                key={id + "container"}
                id={id}
                date={date}
                workouts={workouts}
              ></WorkoutCardContainer>
            ))
          : ""}
      </CardGroup>
    </DndProvider>
  );
};

export default Week;
