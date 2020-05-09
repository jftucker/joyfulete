import React, { useContext } from "react";
import UserContext from "../context/userContext";

const Zones = () => {
  const {
    hrMax,
    hrResting,
    hrAerobicThreshold,
    hrLactateThreshold,
  } = useContext(UserContext);
  const heartRates = {};
  heartRates.range = hrMax - hrResting;
  heartRates.aerobicThresholdWidth = hrAerobicThreshold - hrResting;
  heartRates.lactateThresholdWidth = hrLactateThreshold - hrAerobicThreshold;
  heartRates.recoveryWidth = Math.round(heartRates.aerobicThresholdWidth * 0.8);
  heartRates.z1Width = Math.round(
    heartRates.aerobicThresholdWidth * 0.9 - heartRates.recoveryWidth
  );
  heartRates.z2Width = heartRates.z1Width;
  heartRates.z3Width = heartRates.lactateThresholdWidth;
  heartRates.z4Width = Math.round((hrMax - hrLactateThreshold) * 0.6);
  heartRates.z5Width = Math.round((hrMax - hrLactateThreshold) * 0.4);

  heartRates.recoveryPercentage = Math.round(
    (100 * heartRates.recoveryWidth) / heartRates.range
  );
  heartRates.z1Percentage = Math.round(
    (100 * heartRates.z1Width) / heartRates.range
  );
  heartRates.z2Percentage = Math.round(
    (100 * heartRates.z2Width) / heartRates.range
  );
  heartRates.z3Percentage = Math.round(
    (100 * heartRates.z3Width) / heartRates.range
  );
  heartRates.z4Percentage = Math.round(
    (100 * heartRates.z4Width) / heartRates.range
  );
  heartRates.z5Percentage = Math.round(
    (100 * heartRates.z5Width) / heartRates.range
  );
  heartRates.z1Percentage = Math.round(
    (100 * heartRates.z1Width) / heartRates.range
  );

  return (
    <div className="container">
      <div className="row">
        <div
          className="border border-primary text-center rounded-left d-table"
          style={{ width: `${heartRates.recoveryPercentage}%`, height: "60px" }}
        >
          <span className="d-table-cell align-middle">Recovery</span>
        </div>
        <div
          className="border border-success text-center d-table"
          style={{ width: `${heartRates.z1Percentage}%`, height: "60px" }}
        >
          <span className="d-table-cell align-middle">Z1</span>
        </div>
        <div
          className="border border-success text-center d-table"
          style={{ width: `${heartRates.z2Percentage}%`, height: "60px" }}
        >
          <span className="d-table-cell align-middle">Z2</span>
        </div>
        <div
          className="border border-warning text-center d-table"
          style={{ width: `${heartRates.z3Percentage}%`, height: "60px" }}
        >
          <span className="d-table-cell align-middle">Z3</span>
        </div>
        <div
          className="border border-danger text-center d-table"
          style={{ width: `${heartRates.z4Percentage}%`, height: "60px" }}
        >
          <span className="d-table-cell align-middle">Z4</span>
        </div>
        <div
          className="border border-danger text-center rounded-right d-table"
          style={{ width: `${heartRates.z5Percentage}%`, height: "60px" }}
        >
          <span className="d-table-cell align-middle">Z5</span>
        </div>
      </div>
    </div>
  );
};

export default Zones;
