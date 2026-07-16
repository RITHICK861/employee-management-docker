# Employee Management Multi-Tier Application

A containerized multi-tier Employee Management application built using **Docker Compose** and deployed on **AWS EC2**. The application consists of a frontend, a Flask REST API backend, and a MySQL database, demonstrating modern DevOps deployment practices.

---

## Technologies Used

- AWS EC2 (Ubuntu)
- Docker
- Docker Compose
- Python
- Flask
- MySQL 8
- HTML5
- CSS3
- JavaScript
- Git & GitHub

---

## Project Architecture

```
                User
                 │
                 ▼
        Frontend (Nginx)
                 │
                 ▼
      Flask REST API Backend
                 │
                 ▼
          MySQL Database
```

---

## Features

- Multi-tier application architecture
- Docker containerization
- Docker Compose orchestration
- Flask REST API
- MySQL database integration
- Dynamic employee data retrieval
- AWS EC2 deployment
- Container networking using Docker Compose

---

## Project Structure

```
employee-management-docker/
│
├── Frontend/
│   ├── index.html
│   └── Dockerfile
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

## API Endpoint

### Get Employee Details

```
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

## Running the Project

### Clone the Repository

```bash
git clone https://github.com/RITHICK861/employee-management-docker.git
```

### Navigate to the Project

```bash
cd employee-management-docker
```

### Build and Start Containers

```bash
docker compose up -d --build
```

### Access the Application

```
http://localhost
```

For AWS deployment:

```
http://<EC2-PUBLIC-IP>
```

---

## Docker Services

| Service | Technology | Port |
|----------|------------|------|
| Frontend | Nginx | 80 |
| Backend | Flask | 5000 |
| Database | MySQL 8 | 3306 |

---

## Skills Demonstrated

- Docker Image Creation
- Multi-Container Applications
- Docker Compose
- REST API Development
- MySQL Integration
- AWS EC2 Deployment
- Container Networking
- Git Version Control
- GitHub Repository Management

---

## Future Enhancements

- Jenkins CI/CD Pipeline
- Nginx Reverse Proxy
- HTTPS with SSL
- Docker Hub Integration
- AWS Application Load Balancer
- Monitoring with Prometheus and Grafana

---

## Author

**Rithick K M**

GitHub: https://github.com/RITHICK861