import React, { Fragment } from "react";
import { getWeek } from "../services/weeksService";
import { useState, useEffect } from "react";
import Card from "react-bootstrap/Card";
import CardGroup from "react-bootstrap/CardGroup";

const Week = () => {
  const [week, setWeek] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const result = await getWeek("7b8f7eb2-1742-450d-a2f0-40b8122e6f51");
      setWeek(result.data);
    };

    fetchData();
  }, []);

  const zoneStyle = (zone) => {
    if (zone < 3) {
      return "success";
    } else if (zone === 3) {
      return "warning";
    } else {
      return "danger";
    }
  };

  const day = (date) => {
    const dayOfWeek = new Date(date);

    const weekday = new Array(7);

    weekday[0] = "Monday";
    weekday[1] = "Tuesday";
    weekday[2] = "Wednesday";
    weekday[3] = "Thursday";
    weekday[4] = "Friday";
    weekday[5] = "Saturday";
    weekday[6] = "Sunday";

    return weekday[dayOfWeek.getDay()];
  };

  return (
    <CardGroup>
      {week.days
        ? week.days.map(({ id, date, workouts }) => (
            <Fragment key={id + "fragment"}>
              <Card
                key={id}
                className="text-bold"
                text="dark"
                variant="top"
                border="dark"
              >
                <Card.Header
                  as="h5"
                  key={id + "header"}
                  bg="dark"
                  className="text-center mb-1"
                >
                  <p>{day(date)}</p>
                  <p>{date}</p>
                </Card.Header>
                {workouts.map(({ id, zone, title }) => (
                  <Card
                    key={id}
                    text={zoneStyle(zone)}
                    border={zoneStyle(zone)}
                    className="mb-1 mx-1 p-1"
                  >
                    <Card.Title
                      className="my-auto text-center"
                      as="h6"
                      key={id}
                    >
                      {title}
                    </Card.Title>
                  </Card>
                ))}
              </Card>
            </Fragment>
          ))
        : ""}
    </CardGroup>
  );
};

export default Week;
