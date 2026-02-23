import React, { useEffect, useState } from "react";
import axios from "axios";
import { getToken } from "../utils/auth";

export default function WeeklyPlanList({ onSelect }) {
  const [plans, setPlans] = useState([]);
  useEffect(() => {
    axios.get("/plans", { headers: { Authorization: `Bearer ${getToken()}` } })
      .then(res => setPlans(res.data))
      .catch(() => setPlans([]));
  }, []);
  return (
    <div>
      <h3>All Weekly Plans</h3>
      <ul>
        {plans.map(plan => (
          <li key={plan.id}>
            {plan.work_type} | {plan.product_type} | Qty: {plan.target_quantity} | Status: {plan.status}
            <button onClick={() => onSelect(plan)}>View</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
