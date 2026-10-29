# Docker Full-Stack Application

## Project Overview
This project demonstrates a containerized web application using a Node.js Express frontend and a Python Flask backend. Docker Compose runs both services on a shared network.

## Technologies
- Node.js and Express
- Python and Flask
- Docker
- Docker Compose

## Project Structure
```text
Docker_Vikas/
├── frontend/
│   ├── public/
│   ├── Dockerfile
│   ├── package.json
│   └── server.js
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── screenshots/
├── compose.yaml
├── .gitignore
└── README.md
```

## Run the Application
From the project root, execute:

```powershell
docker compose up --build -d
```

Open the frontend in your browser:

http://localhost:3000

Backend endpoint:

http://localhost:5000

## Stop the Application

```powershell
docker compose down
```

## Docker Hub Images
- Backend: `vvera4739/vikas-flask-backend:1.0`
- Frontend: `vvera4739/vikas-node-frontend:1.0`

## Author
Vikas