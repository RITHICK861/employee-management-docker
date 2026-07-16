# Multi-Tier Employee Management System

## Project Overview

This project is a multi-tier web application built using Docker Compose. It consists of three containers:

- Frontend (Nginx + HTML + JavaScript)
- Backend (Flask REST API)
- MySQL Database

The frontend communicates with the Flask backend, and the backend retrieves employee data from the MySQL database.

## Technologies Used

- Docker
- Docker Compose
- Nginx
- Flask
- MySQL
- HTML
- JavaScript
- Git
- GitHub

## Project Architecture

Browser
↓
Nginx Frontend
↓
Flask Backend API
↓
MySQL Database

## Features

- View employee details
- REST API integration
- Docker networking
- Multi-container deployment
- Database initialization using SQL script

## Run the Project

```bash
docker compose up --build
```

Open:

- Frontend: http://localhost
- Backend API: http://localhost:5000/employees

## Author

Rithick km