import _ from "lodash";

export const moveWorkout = (fromDay, toDay, fromProps, toProps) => {
  const newWeek = { ...fromProps.week };
  const newDays = newWeek.days.filter(
    item => item.id !== toProps.dayId && item.id !== fromProps.id
  );
  const workout = _.find(fromDay.workouts, obj => obj.id === toProps.id);

  fromDay.workouts = fromDay.workouts.filter(
    workout => workout.id !== toProps.id
  );
  toDay.workouts = [...toDay.workouts, workout];

  newWeek.days = [...newDays, toDay, fromDay].sort((a, b) =>
    a.date > b.date ? 1 : -1
  );

  fromProps.setWeek(newWeek);
};
