import React from "react";
import { getWeek } from "../services/weeksService";
import { useState, useEffect } from "react";
import { DndProvider } from "react-dnd";
import Backend from "react-dnd-html5-backend";
import CardGroup from "react-bootstrap/CardGroup";
import WorkoutCardContainer from "./WorkoutCardContainer";

const Week = ({ id: weekId }) => {
  const [week, setWeek] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const result = await getWeek(weekId);
      setWeek(result.data);
    };

    fetchData();
  }, [weekId]);

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
                week={week}
                setWeek={setWeek}
              ></WorkoutCardContainer>
            ))
          : ""}
      </CardGroup>
    </DndProvider>
  );
};

export default Week;
