# Task Manager - Full Stack Project

This project is a full-stack Task Management System built using Next.js (frontend) and FastAPI (backend). It allows users to create, view, update, and delete tasks with secure JWT-based authentication.


🚀 Features

- Create tasks
- View all tasks
- Update task status
- Delete tasks
- Set task priority (Low / Medium / High)
- JWT-based login authentication
- Task summary (Pending / Completed count)


🛠️ Tech Stack

Frontend
- Next.js (App Router)
- React

Backend
- FastAPI
- Python

Database
- SQLite

Authentication
- JWT (JSON Web Token)


⚙️ Setup Instructions

🔹 Clone the Repository

git clone https://github.com/YOUR_USERNAME/task-manager-fullstack.git
cd task-manager-fullstack

🔹 Backend Setup

cd backend
pip install fastapi uvicorn python-multipart
python -m uvicorn main:app --reload

Backend runs on:
http://127.0.0.1:8000/docs

🔹 Frontend Setup

cd frontend
npm install
npm run dev

Frontend runs on:
http://localhost:3000


🔐 Authentication

Users login using username and password
JWT token is generated and stored in browser
Token is used for secure API requests


📊 API Endpoints

Method	       Endpoint	         Description
POST	        /login	         User login
POST	        /tasks	         Create task
GET	            /tasks	         Get all tasks
GET	            /tasks/{id}	     Get single task
PUT	            /tasks/{id}	     Update task
DELETE	        /tasks/{id}	     Delete task


🧠 Tech Decisions

FastAPI chosen for high performance and automatic API documentation
Next.js used for building modern frontend with routing
SQLite used for simplicity and easy setup
JWT Authentication ensures secure and stateless communication


⚠️ Limitations

No multi-user system
No deadline feature
No notifications
No cloud deployment


🔮 Future Improvements

Add task deadlines and reminders
Implement multi-user login system
Add search and filter functionality
Deploy project on cloud (Vercel + Render)
Add AI-based task suggestions


📸 Application Preview

Login & Authentication
Dashboard & Task Analytics
Task Page


👨‍💻 Author

Kritika Sharma - kritikasharma0208@gmail.com
GitHub Profile - https://github.com/KritikaSharma2402