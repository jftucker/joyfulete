const zoneStyle = (zone) => {
  if (zone < 3) {
    return "success";
  } else if (zone === 3) {
    return "warning";
  } else {
    return "danger";
  }
};

export default zoneStyle;
