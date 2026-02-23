import React, { useState } from "react";
import axios from "axios";
import { getToken } from "../utils/auth";

export default function WeeklyPlanAssign({ onAssigned }) {
  const [form, setForm] = useState({
    assigned_to: "",
    work_type: "Repair",
    receipt_number: "",
    order_number: "",
    for_stock: false,
    product_type: "",
    task_description: "",
    target_quantity: 1,
    deadline: "",
    required_materials: []
  });
  const [error, setError] = useState("");

  const handleChange = e => {
    const { name, value, type, checked } = e.target;
    setForm(f => ({ ...f, [name]: type === "checkbox" ? checked : value }));
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setError("");
    try {
      await axios.post("/plans/assign", form, { headers: { Authorization: `Bearer ${getToken()}` } });
      onAssigned && onAssigned();
    } catch (err) {
      setError(err.response?.data?.detail || "Error assigning plan");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Assign Weekly Plan</h3>
      <input name="assigned_to" placeholder="Employee ID" value={form.assigned_to} onChange={handleChange} required />
      <select name="work_type" value={form.work_type} onChange={handleChange} required>
        <option>Repair</option>
        <option>Custom Order</option>
        <option>Stock Production</option>
      </select>
      {form.work_type === "Repair" && (
        <input name="receipt_number" placeholder="Receipt #" value={form.receipt_number} onChange={handleChange} required />
      )}
      {form.work_type === "Custom Order" && (
        <input name="order_number" placeholder="Order/Invoice #" value={form.order_number} onChange={handleChange} required />
      )}
      {form.work_type === "Stock Production" && (
        <label>
          <input type="checkbox" name="for_stock" checked={form.for_stock} onChange={handleChange} /> FOR STOCK
        </label>
      )}
      <input name="product_type" placeholder="Product Type" value={form.product_type} onChange={handleChange} required />
      <input name="task_description" placeholder="Task Description" value={form.task_description} onChange={handleChange} required />
      <input name="target_quantity" type="number" min="1" placeholder="Target Quantity" value={form.target_quantity} onChange={handleChange} required />
      <input name="deadline" type="date" value={form.deadline} onChange={handleChange} required />
      {/* TODO: Add required_materials selection */}
      <button type="submit">Assign</button>
      {error && <div style={{ color: "red" }}>{error}</div>}
    </form>
  );
}
