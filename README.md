# Smart CRM + AI Bot

Universal CRM system built on **Odoo 19**, demonstrating end-to-end business process integration: CRM → Sales → Invoicing → Purchase → Inventory → Manufacturing (MRP).

## 🎯 Purpose

This project was built as a hands-on learning exercise to master Odoo's core business modules and their real-world interconnections — going beyond CRUD operations into cross-module business logic, computed fields, and custom automation.

## 🚀 Features

### Core CRM & Sales
- Extended `res.partner` with computed financial fields (`total_due_amount`, `unpaid_invoice_count`) based on real invoice data
- Automatic `last_contact_date` tracking via `sale.order` confirmation override
- Full CRM Lead → Sale Order → Invoice → Partner update chain, tested end-to-end

### Inventory & Purchasing
- Product variant management (color-based variants) with independent stock tracking per variant
- Purchase Order → Receipt → Inventory flow with unit-of-measure handling (m, units, etc.)
- Manual and Purchase-driven stock replenishment

### Manufacturing (MRP)
- Bill of Materials (BoM) configuration with multi-component recipes
- Manufacturing Orders with automatic component quantity scaling
- Variant-agnostic BoM (applies across all product color variants)

### Custom Automation
- **Inventory availability check on CRM "Won" stage**: when an opportunity is marked as Won, the system automatically checks whether the linked Sale Order's products are sufficiently available in stock. If not, a warning is:
  - Posted to the opportunity's chatter
  - Displayed as a red banner directly on the opportunity form
  - Shown as a badge on the Kanban pipeline card — visible without opening the record

This required overriding `crm.lead.write()`, cross-model queries (`sale.order` → `crm.lead` via `opportunity_id`), and inherited Kanban/Form views with custom Bootstrap-styled alerts.

## 🛠️ Tech Stack

- **Odoo 19** (Community)
- **PostgreSQL 15**
- **Docker Compose** (multi-container: Odoo + PostgreSQL)
- Python (Odoo ORM)

## 📦 Setup

```bash
docker compose up -d
docker compose exec odoo odoo -d <db_name> -i smart_crm
```

Access at `http://localhost:8069`

## 📚 What I Learned

- Odoo module architecture and the importance of not duplicating standard functionality (e.g. relying on `mail.thread`/`mail.activity.mixin` instead of building custom activity models)
- The critical difference between updating a module (`-u`) and restarting the server — Python code changes require a full container restart, while XML/CSV changes only need a module update
- Debugging Odoo with `odoo shell`, logging (`_logger.info`), and real-time log tailing (`docker compose logs -f`)
- Product variant architecture and its implications for BoM, purchasing, and stock tracking
- Cross-module business logic: connecting CRM outcomes to real-time inventory state

## 👤 Author

Ismatillo Ismatov  
[GitHub](https://github.com/ismatillo-ismatov) · [LinkedIn](https://linkedin.com/in/ismatov-ismatillo)
