import Logo from "../components/Logo";
// Placeholder for Employee Dashboard component
import { logout } from "../utils/auth";
import EmployeePlanList from "../components/EmployeePlanList";
import DailyReportSubmit from "../components/DailyReportSubmit";
import MaterialUsageSummary from "../components/MaterialUsageSummary";
import React, { useState } from "react";

export default function EmployeeDashboard() {
  const [selectedPlan, setSelectedPlan] = useState(null);
  return (
    <div>
      <Logo size={72} />
      <h1>Employee Dashboard</h1>
      <button onClick={logout}>Logout</button>
      <EmployeePlanList onSelect={setSelectedPlan} />
      {selectedPlan && selectedPlan.status === "Accepted" && (
        <DailyReportSubmit plan={selectedPlan} onSubmitted={() => setSelectedPlan(null)} />
      )}
      <MaterialUsageSummary />
      {/* TODO: Add daily reports, progress views */}
    </div>
  );
}
