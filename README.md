# CItyBestSchoolDatabase
CBISM database
# 🎓 CityBest School Management System

A full-featured school data management system built with **Python** and **MySQL**, designed to streamline administrative tasks, academic records, and reporting at CityBest International Montessori School.

---

## 📌 Features

- 🔐 Admin & Teacher login (role-based access)
- 👨‍🏫 Teacher and student data management
- 🗓️ Attendance tracking
- 📊 Academic record storage
- 📤 Automatic Excel and PDF report generation
- 🎛️ Dynamic class management and reporting
- 🧮 Integrated MySQL-Python backend

---

## 🖥️ Technologies Used

- 🐍 Python 3 (with Tkinter for GUI)
- 🐬 MySQL
- 📊 Pandas & openpyxl (Excel support)
- 📄 FPDF or ReportLab (PDF generation)
- 💾 WSL Ubuntu environment

---

## 📷 Screenshots

> _(Add these images in a folder named `assets/`)_

![Login Page](assets/login_page.png)
![Dashboard](assets/dashboard.png)
![Report Generation](assets/report_page.png)

---

## 🧠 Project Structure

```bash
citybest_school_system/
├── citybest_gui.py             # GUI frontend
├── city_best_school_system.py  # Core system logic
├── create_table.py             # DB setup script
├── insert_data.py              # Sample data insert script
├── mysql_test.py               # DB connection testing
├── students.xlsx               # Sample data file
├── students.pdf                # Sample PDF report
└── assets/                     # Screenshots and visuals

