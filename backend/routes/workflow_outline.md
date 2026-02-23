# Weekly Plan and Daily Report Workflow Outline
# This file documents the endpoints and logic for plan/report workflows

# Weekly Plan Endpoints (Admin)
# - POST /plans/assign: Assign weekly plan to employee (with validation)
# - PUT /plans/{id}/edit: Edit plan before acceptance
# - GET /plans: List all plans (filter by status, employee, etc.)
# - GET /plans/{id}: View plan details

# Weekly Plan Endpoints (Employee)
# - POST /plans/{id}/accept: Accept assigned plan
# - GET /plans/assigned: View assigned plans

# Daily Report Endpoints (Employee)
# - POST /reports/submit: Submit daily report (auto-link to plan, validate fields)
# - GET /reports/mine: View own reports

# Daily Report Endpoints (Supervisor)
# - GET /reports/pending: View reports pending confirmation
# - POST /reports/{id}/confirm: Confirm report
# - POST /reports/{id}/reject: Reject report (with reason)

# Daily Report Endpoints (Admin)
# - GET /reports/for-approval: View reports pending admin approval
# - POST /reports/{id}/approve: Approve report (final)
# - POST /reports/{id}/reject: Reject report (with reason)

# All endpoints must enforce role-based access and status transitions.
# All actions must be logged in the audit log.
