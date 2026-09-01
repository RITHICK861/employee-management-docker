# 🚀 Employee Management Multi-Tier Application

A containerized **Employee Management System** built using **Docker Compose** and deployed on **AWS EC2**. This project demonstrates a complete multi-tier architecture where the frontend communicates with a Flask REST API, which interacts with a MySQL database running in separate Docker containers.

---

## 📌 Project Overview

This project showcases modern DevOps deployment practices by separating the application into three independent containers:

- 🌐 Frontend (Nginx + HTML + CSS + JavaScript)
- ⚙️ Backend (Python Flask REST API)
- 🗄️ MySQL Database

All services are orchestrated using **Docker Compose** and deployed on an **AWS EC2 Ubuntu** instance.

---

# 🏗️ Architecture

```text
                          Employee Management Application

                              +----------------------+
                              |        User          |
                              |      (Browser)       |
                              +----------+-----------+
                                         |
                                 HTTP Request (80)
                                         |
                                         ▼
                  +---------------------------------------+
                  |        AWS EC2 (Ubuntu Server)        |
                  |       Docker + Docker Compose         |
                  +---------------------------------------+
                                │
         ---------------------------------------------------------
         │                        │                             │
         ▼                        ▼                             ▼
+------------------+     +--------------------+      +----------------------+
| Frontend         |     | Backend            |      | MySQL Database       |
| Nginx            | --> | Flask REST API     | -->  | MySQL 8              |
| HTML             |     | Python             |      | companydb            |
| CSS              |     | mysql-connector    |      | employees table      |
| JavaScript       |     | Port:5000          |      | Port:3306            |
| Port:80          |     +--------------------+      +----------------------+
```

---

# 🔄 Application Workflow

```text
User
   │
   ▼
Open EC2 Public IP
   │
   ▼
Nginx serves Frontend
   │
   ▼
Click "Load Employees"
   │
   ▼
JavaScript sends GET request
   │
   ▼
Flask REST API (/employees)
   │
   ▼
MySQL Database
   │
   ▼
Employee Records
   │
   ▼
JSON Response
   │
   ▼
Employees displayed in Browser
```

---

# ✨ Features

- Multi-Tier Architecture
- Docker Containerization
- Docker Compose Orchestration
- Flask REST API
- MySQL Database Integration
- Dynamic Employee Data Retrieval
- AWS EC2 Deployment
- Container Networking
- RESTful API Communication

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| AWS EC2 | Cloud Hosting |
| Ubuntu | Operating System |
| Docker | Containerization |
| Docker Compose | Container Orchestration |
| Nginx | Frontend Web Server |
| Python | Backend Language |
| Flask | REST API Framework |
| MySQL 8 | Database |
| HTML5 | Frontend |
| CSS3 | Styling |
| JavaScript | Dynamic UI |
| Git & GitHub | Version Control |

---

# 📂 Project Structure

```text
employee-management-docker/
│
├── Frontend/
│   ├── index.html
│   ├── Dockerfile
│   └── nginx.conf
│
├── Backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── Database/
│   └── init.sql
│
├── docker-compose.yml
└── README.md
```

---

# 🔗 API Endpoint

## Get Employee Details

```http
GET /employees
```

### Sample Response

```json
[
  {
    "id": 1,
    "name": "Rithick",
    "department": "DevOps"
  },
  {
    "id": 2,
    "name": "Rahul",
    "department": "Developer"
  },
  {
    "id": 3,
    "name": "Priya",
    "department": "Testing"
  }
]
```

---

# ▶️ Running the Project

### Clone Repository

```bash
git clone https://github.com/RITHICK861/employee-management-docker.git
```

### Navigate

```bash
cd employee-management-docker
```

### Build & Run

```bash
docker compose up -d --build
```

---

# 🌐 Access Application

### Local

```
http://localhost
```

### AWS EC2

```
http://<EC2-PUBLIC-IP>
```

---

# 🐳 Docker Services

| Service | Technology | Port | Description |
|----------|------------|------|-------------|
| Frontend | Nginx | 80 | Serves the web application |
| Backend | Flask | 5000 | REST API |
| Database | MySQL 8 | 3306 | Stores employee data |

---

# 💡 Skills Demonstrated

- Docker
- Docker Compose
- Multi-Container Applications
- REST API Development
- MySQL Integration
- AWS EC2 Deployment
- Container Networking
- Linux Administration
- Git & GitHub

---

# 🚀 Future Enhancements

- Jenkins CI/CD Pipeline
- HTTPS using SSL
- Docker Hub Integration
- AWS Application Load Balancer
- Monitoring with Prometheus & Grafana

---

# 👨‍💻 Author

**Rithick K M**

GitHub: https://github.com/RITHICK861

---
