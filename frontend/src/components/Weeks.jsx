import React, { useState, useEffect, Fragment } from "react";
import Week from "./Week";
import { getWeeks } from "../services/weeksService";

const Weeks = () => {
  const [weeks, setWeeks] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await getWeeks();
      setWeeks(result.data);
    };

    fetchData();
  }, []);

  return (
    <Fragment>
      {weeks
        ? weeks.map((week) => <Week key={week.id} id={week.id}></Week>)
        : ""}
    </Fragment>
  );
};

export default Weeks;
