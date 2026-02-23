import Logo from "../components/Logo";
// Placeholder for Supervisor Dashboard component
import { logout } from "../utils/auth";
import SupervisorReportList from "../components/SupervisorReportList";
import MaterialUsageSummary from "../components/MaterialUsageSummary";

export default function SupervisorDashboard() {
  return (
    <div>
      <Logo size={72} />
      <h1>Supervisor Dashboard</h1>
      <button onClick={logout}>Logout</button>
      <SupervisorReportList />
      <MaterialUsageSummary />
      {/* TODO: Add employee performance views */}
    </div>
  );
}
