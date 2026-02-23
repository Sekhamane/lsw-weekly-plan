import React, { useEffect, useState } from "react";
import axios from "axios";
import { getToken } from "../utils/auth";

export default function MaterialUsageSummary() {
  const [usage, setUsage] = useState([]);
  useEffect(() => {
    axios.get("/materials/usage-summary", { headers: { Authorization: `Bearer ${getToken()}` } })
      .then(res => setUsage(res.data))
      .catch(() => setUsage([]));
  }, []);
  return (
    <div>
      <h3>Material Usage Summary</h3>
      <table border="1" cellPadding="4">
        <thead>
          <tr>
            <th>Material</th>
            <th>Unit</th>
            <th>Quantity Used</th>
            <th>Report ID</th>
            <th>Employee ID</th>
          </tr>
        </thead>
        <tbody>
          {usage.map((u, i) => (
            <tr key={i}>
              <td>{u.material}</td>
              <td>{u.unit}</td>
              <td>{u.quantity_used}</td>
              <td>{u.report_id}</td>
              <td>{u.employee_id}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
