# Material Control and Inventory Logic Outline
# This file documents the logic and endpoints for material usage and inventory

# Material Usage
# - Materials are linked to weekly plans and daily reports
# - Employees log materials used per report
# - Supervisors verify material usage (cannot edit)
# - Admin approves material usage (final)
# - Material is deducted from inventory ONLY after admin approval
# - System tracks usage per employee, plan, order, repair, and stock
# - Weekly material summary and overuse alerts

# Inventory Endpoints (Admin only)
# - GET /materials/inventory: View inventory levels
# - POST /materials/add: Add new material or restock
# - PUT /materials/{id}/update: Update material info
# - GET /materials/usage-summary: View usage summary

# Material Usage Endpoints
# - GET /materials/usage: View material usage (role-based filtering)

# All actions must be logged in the audit log.
