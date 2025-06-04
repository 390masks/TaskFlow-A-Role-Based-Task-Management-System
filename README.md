# 📝 TaskFlow – Role-Based Task Management System (Backend)

TaskFlow is a powerful task management backend system built with Django and Django REST Framework (DRF). It supports **role-based access control (RBAC)** with three key user roles:
- 🛠️ **Admin** – Full access
- 👨‍💼 **Manager** – Can create and assign tasks
- 👤 **Member** – Can view and update assigned tasks

---

## 🚀 Features

- ✅ User Registration, Login (JWT), Logout (Token Blacklisting)
- 🔐 Password Change functionality
- 👥 Role-based access control (Admin, Manager, Member)
- 📁 Project and Team Management
- 📌 Task Creation, Assignment, Update, Deletion
- 🔔 User Notifications
- 🧾 Activity Logging
- 📖 Swagger API documentation

---

## 🛠️ Technologies Used

- Python 3.x
- Django 5.x
- Django REST Framework
- Simple JWT for Authentication
- PostgreSQL (can switch to SQLite for testing)
- drf-yasg for API Docs
- PyTest/Django TestCase (for testing)
- CORS enabled for frontend integration

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/390masks/TaskFlow-A-Role-Based-Task-Management-System.git
cd taskflow
