// Placeholder for Admin Dashboard component
import { logout } from "../utils/auth";
import WeeklyPlanAssign from "../components/WeeklyPlanAssign";
import WeeklyPlanList from "../components/WeeklyPlanList";
import MaterialUsageSummary from "../components/MaterialUsageSummary";
import AuditLogView from "../components/AuditLogView";
import Logo from "../components/Logo";
import React, { useState } from "react";

export default function AdminDashboard() {
  const [refresh, setRefresh] = useState(false);
  return (
    <div>
      <Logo size={72} />
      <h1>Admin Dashboard</h1>
      <button onClick={logout}>Logout</button>
      <WeeklyPlanAssign onAssigned={() => setRefresh(r => !r)} />
      <WeeklyPlanList key={refresh} onSelect={plan => alert(JSON.stringify(plan, null, 2))} />
      <MaterialUsageSummary />
      <AuditLogView />
      {/* TODO: Add report approval, analytics, inventory views */}
    </div>
  );
}
