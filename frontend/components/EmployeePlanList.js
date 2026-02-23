import React, { useEffect, useState } from "react";
import axios from "axios";
import { getToken } from "../utils/auth";

export default function EmployeePlanList({ onSelect }) {
  const [plans, setPlans] = useState([]);
  useEffect(() => {
    axios.get("/plans/assigned", { headers: { Authorization: `Bearer ${getToken()}` } })
      .then(res => setPlans(res.data))
      .catch(() => setPlans([]));
  }, []);
  return (
    <div>
      <h3>My Weekly Plans</h3>
      <ul>
        {plans.map(plan => (
          <li key={plan.id}>
            {plan.work_type} | {plan.product_type} | Qty: {plan.target_quantity} | Status: {plan.status}
            <button onClick={() => onSelect(plan)}>View</button>
            {plan.status === "Assigned" && (
              <button onClick={() => acceptPlan(plan.id)}>Accept</button>
            )}
          </li>
        ))}
      </ul>
    </div>
  );

  function acceptPlan(planId) {
    axios.post(`/plans/${planId}/accept`, {}, { headers: { Authorization: `Bearer ${getToken()}` } })
      .then(() => window.location.reload())
      .catch(() => alert("Error accepting plan"));
  }
}
