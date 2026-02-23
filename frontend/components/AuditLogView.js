import React, { useEffect, useState } from "react";
import axios from "axios";
import { getToken } from "../utils/auth";

export default function AuditLogView() {
  const [logs, setLogs] = useState([]);
  useEffect(() => {
    axios.get("/audit/logs", { headers: { Authorization: `Bearer ${getToken()}` } })
      .then(res => setLogs(res.data))
      .catch(() => setLogs([]));
  }, []);
  return (
    <div>
      <h3>Audit Log</h3>
      <table border="1" cellPadding="4">
        <thead>
          <tr>
            <th>Action</th>
            <th>User ID</th>
            <th>Target Type</th>
            <th>Target ID</th>
            <th>Timestamp</th>
            <th>Details</th>
          </tr>
        </thead>
        <tbody>
          {logs.map(log => (
            <tr key={log.id}>
              <td>{log.action}</td>
              <td>{log.user_id}</td>
              <td>{log.target_type}</td>
              <td>{log.target_id}</td>
              <td>{log.timestamp}</td>
              <td>{log.details}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
