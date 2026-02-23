import React, { useState } from "react";
import axios from "axios";
import { getToken } from "../utils/auth";

export default function DailyReportSubmit({ plan, onSubmitted }) {
  const [form, setForm] = useState({
    weekly_plan_id: plan.id,
    task_worked_on: "",
    quantity_completed: 0,
    progress_percent: 0,
    issues: "",
    materials_used: []
  });
  const [error, setError] = useState("");

  const handleChange = e => {
    const { name, value } = e.target;
    setForm(f => ({ ...f, [name]: value }));
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setError("");
    try {
      await axios.post("/reports/submit", form, { headers: { Authorization: `Bearer ${getToken()}` } });
      onSubmitted && onSubmitted();
    } catch (err) {
      setError(err.response?.data?.detail || "Error submitting report");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h4>Submit Daily Report for Plan #{plan.id}</h4>
      <input name="task_worked_on" placeholder="Task Worked On" value={form.task_worked_on} onChange={handleChange} required />
      <input name="quantity_completed" type="number" min="0" placeholder="Quantity Completed" value={form.quantity_completed} onChange={handleChange} required />
      <input name="progress_percent" type="number" min="0" max="100" placeholder="Progress %" value={form.progress_percent} onChange={handleChange} required />
      <input name="issues" placeholder="Issues (optional)" value={form.issues} onChange={handleChange} />
      {/* TODO: Add materials_used input */}
      <button type="submit">Submit Report</button>
      {error && <div style={{ color: "red" }}>{error}</div>}
    </form>
  );
}
