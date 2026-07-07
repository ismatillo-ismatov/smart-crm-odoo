# Smart CRM - Odoo 19 Custom Module

Custom Odoo 19 module that extends standard CRM, Sales and Accounting with unified activity tracking.

## Features

- **res.partner** extended with accounting metrics (unpaid invoices, total due amount, last contact date)
- **crm.activity** — custom model for tracking calls, meetings and emails linked to both partners and CRM leads
- **crm.lead** extended with custom activity history tab
- **sale.order** — auto-updates partner's last contact date on order confirmation
- Full security (ir.model.access.csv), views, actions and menus

## Tech Stack

- Odoo 19 (Docker)
- PostgreSQL 15
- Python 3.12

## Models

| Model | Type | Description |
|-------|------|-------------|
| `res.partner` | inherit | Accounting metrics + constraint |
| `crm.activity` | new | Activity tracking model |
| `crm.lead` | inherit | Custom activity tab |
| `sale.order` | inherit | Auto last_contact_date update |

## Author

Ismatillo Ismatov — Python/Django/Odoo Backend Developer
