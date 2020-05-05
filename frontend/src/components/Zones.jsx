import React from "react";

const Zones = () => {
  return (
    <div className="container">
      <div className="row">
        <div
          className="border border-primary text-center rounded-left"
          style={{ width: "20%", height: "60px" }}
        >
          Recovery
        </div>
        <div
          className="border border-success text-center"
          style={{ width: "25%", height: "60px" }}
        >
          Z1
        </div>
        <div
          className="border border-success text-center"
          style={{ width: "25%", height: "60px" }}
        >
          Z2
        </div>
        <div
          className="border border-warning text-center"
          style={{ width: "15%", height: "60px" }}
        >
          Z3
        </div>
        <div
          className="border border-danger text-center"
          style={{ width: "8%", height: "60px" }}
        >
          Z4
        </div>
        <div
          className="border border-danger text-center rounded-right"
          style={{ width: "7%", height: "60px" }}
        >
          Z5
        </div>
      </div>
    </div>
  );
};

export default Zones;
