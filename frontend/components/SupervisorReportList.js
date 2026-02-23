import React, { useEffect, useState } from "react";
import axios from "axios";
import { getToken } from "../utils/auth";

export default function SupervisorReportList() {
  const [reports, setReports] = useState([]);
  const [comment, setComment] = useState("");
  useEffect(() => {
    axios.get("/reports/pending", { headers: { Authorization: `Bearer ${getToken()}` } })
      .then(res => setReports(res.data))
      .catch(() => setReports([]));
  }, []);

  function confirmReport(id) {
    axios.post(`/reports/${id}/confirm`, {}, { headers: { Authorization: `Bearer ${getToken()}` } })
      .then(() => window.location.reload())
      .catch(() => alert("Error confirming report"));
  }

  function rejectReport(id) {
    if (!comment) return alert("Please enter a rejection reason.");
    axios.post(`/reports/${id}/reject`, null, {
      params: { comment },
      headers: { Authorization: `Bearer ${getToken()}` }
    })
      .then(() => window.location.reload())
      .catch(() => alert("Error rejecting report"));
  }

  return (
    <div>
      <h3>Reports Pending Confirmation</h3>
      <ul>
        {reports.map(r => (
          <li key={r.id}>
            Plan #{r.weekly_plan_id} | Qty: {r.quantity_completed} | Progress: {r.progress_percent}%
            <button onClick={() => confirmReport(r.id)}>Confirm</button>
            <input
              placeholder="Rejection reason"
              value={comment}
              onChange={e => setComment(e.target.value)}
              style={{ marginLeft: 8 }}
            />
            <button onClick={() => rejectReport(r.id)}>Reject</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
