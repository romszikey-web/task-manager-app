# 📝 Task Manager

A simple task manager web app built with **Flask**, **SQLAlchemy**, and **Flask-Login**.  
Users can register, log in, add tasks, mark them as completed, and manage their personal to-do list.  

## 🚀 Features
- User authentication (Login/Signup/Logout)
- Add, edit, and delete tasks
- Mark tasks as completed
- Flash messages for actions
- Responsive design with Bootstrap 5

## 🛠 Tech Stack
- Python 3
- Flask
- SQLAlchemy
- Flask-Login
- Bootstrap 5

## ⚡ Installation

Clone the repository:
```bash
git clone https://github.com/romszikey-web/task-manager-app.git
cd task-manager-app

(On Windows PowerShell):

python -m venv venv
venv\Scripts\activate


(On Mac/Linux):

python3 -m venv venv
source venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set up the database

When you run the app for the first time, it will automatically create the SQLite database (task.db).

4️⃣ Run the app locally
flask run


or if you use the create_app() factory:

python -m flask run


The app will be available at:
👉 http://127.0.0.1:5000