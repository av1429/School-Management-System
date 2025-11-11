# 🏫 School Management System (Python + MySQL)

## 📄 Overview
This project is a **console-based School Management System** built using **Python and MySQL**, designed to manage student records efficiently.  
It supports adding, viewing, searching, modifying, and deleting student details through a user-friendly menu-driven interface.

---

## ⚙️ Features
- 🧾 Add, display, modify, and delete student records.  
- 🔍 Search records by **Roll Number** or **Name**.  
- 🗄️ Stores all data in a **MySQL database** (`studentdetails` table).  
- 📋 Input validation for **Phone Number** and **Aadhaar Number**.  
- 💾 Automatic commit of all database changes in real-time.

---

## 🧮 Database Structure
| Field | Type | Description |
|:------|:------|:-------------|
| Roll No | VARCHAR | Unique identifier for each student |
| Admission No | VARCHAR | Admission ID |
| Name | VARCHAR | Student name |
| Class | VARCHAR | Academic class |
| DOB | VARCHAR | Date of birth |
| Father Name | VARCHAR | — |
| Mother Name | VARCHAR | — |
| Phone | INT | 10-digit mobile number |
| Aadhaar | INT | 12-digit ID number |
| Email | VARCHAR | Email address |
| Stream | VARCHAR | Academic stream |
| Percentage | VARCHAR | Marks or grade |
| Blood Group | VARCHAR | Blood group type |
| Address | VARCHAR | Residential address |

---

## 💻 How to Run
1. Install required package:
   ```bash
   pip install mysql-connector-python

2. Create a MySQL database:
   ```bash
   CREATE DATABASE sms;
    USE sms;
    CREATE TABLE studentdetails (
        rollno VARCHAR(10),
        admnno VARCHAR(10),
        name VARCHAR(50),
        class VARCHAR(10),
        dob VARCHAR(15),
        fname VARCHAR(50),
        mname VARCHAR(50),
        phone BIGINT,
        aadhaar BIGINT,
        email VARCHAR(50),
        stream VARCHAR(20),
        per VARCHAR(5),
        bloodgroup VARCHAR(10),
        address VARCHAR(100)
    );

3. Update the connection in code:

  ```python
    mycon = ms.connect(host='localhost', user='root', passwd='YOUR_PASSWORD', database='sms')
  ```

4. Run the program:
  ```python
    python school_management_system.py
  ```

---

## 🧰 Tools & Technologies

- **Language:** Python
- **Database:** MySQL
- **Libraries:** mysql.connector, os
- **Platform:** Windows / Linux
  
---

## 🚀 Future Enhancements

- GUI version using Tkinter or PyQt.
- Integration of attendance and grading modules.
- Export reports to Excel or PDF.

---

### 👨‍💻 Author

**Aravinthvasan S**  
Kendriya Vidyalaya, Karaikudi
🔗 [GitHub Profile](https://github.com/av1429)

---

## 🪪 License

Licensed under the MIT License — free to use, modify, and distribute with attribution.


