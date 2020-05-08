import React from "react";

const Zones = () => {
  return (
    <div className="container">
      <div className="row">
        <div
          className="border border-primary text-center rounded-left d-table"
          style={{ width: "20%", height: "60px" }}
        >
          <span className="d-table-cell align-middle">Recovery</span>
        </div>
        <div
          className="border border-success text-center d-table"
          style={{ width: "25%", height: "60px" }}
        >
          <span className="d-table-cell align-middle">Z1</span>
        </div>
        <div
          className="border border-success text-center d-table"
          style={{ width: "25%", height: "60px" }}
        >
          <span className="d-table-cell align-middle">Z2</span>
        </div>
        <div
          className="border border-warning text-center d-table"
          style={{ width: "15%", height: "60px" }}
        >
          <span className="d-table-cell align-middle">Z3</span>
        </div>
        <div
          className="border border-danger text-center d-table"
          style={{ width: "8%", height: "60px" }}
        >
          <span className="d-table-cell align-middle">Z4</span>
        </div>
        <div
          className="border border-danger text-center rounded-right d-table"
          style={{ width: "7%", height: "60px" }}
        >
          <span className="d-table-cell align-middle">Z5</span>
        </div>
      </div>
    </div>
  );
};

export default Zones;
