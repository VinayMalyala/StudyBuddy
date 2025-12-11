# 🧠 StudyBuddy  
A full-stack **Django-based discussion platform** inspired by Discord, designed for learning communities to collaborate, create rooms, and engage in topic-focused conversations.

---

## 📌 Overview  
StudyBuddy is a full-stack collaborative web application built with **Django**, designed to replicate a lightweight version of Discord’s room-based discussion system. The platform enables students, developers, and learning communities to organize conversations into topic-focused rooms, promoting structured and meaningful interaction.

Users can:
- Join or create dedicated **study rooms** for any subject or topic  
- Post messages, ask questions, and engage in threaded discussions  
- Search rooms efficiently using keywords or topics  
- Update or delete their own rooms and messages  
- Manage their identity with Django’s built-in user authentication  

The goal of StudyBuddy is to provide a minimal, elegant, and intuitive communication platform that supports project collaboration, group study sessions, and community learning. With clearly defined rooms, searchable content, and a user-friendly UI, the application offers a clean alternative to traditional chat apps while maintaining flexibility for expansion into larger community features.

All application data—including users, messages, and room metadata—is stored securely in a **SQLite database**, making the project lightweight, easy to deploy, and ideal for portfolio demonstration or extensible development.

---

## 🏗️ Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Frontend** | HTML, CSS, JavaScript, Django Templates |
| **Backend** | Python, Django (MVT Architecture) |
| **Database** | SQLite |
| **Other** | Django ORM, Django Authentication |

---

## ✨ Key Features

### 🔐 User Authentication
- &nbsp;&nbsp; Register, login, logout  
- &nbsp;&nbsp; Create and manage user profiles  

### 💬 Rooms & Conversations
- &nbsp;&nbsp; Create, update, delete rooms  
- &nbsp;&nbsp; Participate in message threads  
- &nbsp;&nbsp; Room hosts can control their space  

### 🔎 Smart Search
- &nbsp;&nbsp; Search rooms by topic or room name  
- &nbsp;&nbsp; Explore discussions efficiently  

### 📁 Database Integration
- &nbsp;&nbsp; SQLite for room, user, and message persistence  
- &nbsp;&nbsp; Django ORM for secure and optimized database operations  

---

## 📸 Screenshots  
> Add screenshots of your UI here  


---

## 🚀 Getting Started

### &nbsp;&nbsp; 1. Clone the Repository
```bash
git clone https://github.com/VinayMalyala/StudyBuddy.git
cd StudyBuddy
```

### &nbsp;&nbsp; 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### &nbsp;&nbsp; 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### &nbsp;&nbsp; 4. Run Migrations
```bash
python manage.py migrate
```

### &nbsp;&nbsp; 5. Start the Development Server
```bash
python manage.py runserver
```
---

## 📂 Project Structure
```csharp
StudyBuddy/
│── main/              # Core application (rooms, messages, views)
│── templates/         # HTML templates
│── static/            # CSS, JS, images
│── db.sqlite3         # Database
│── manage.py          # Django admin utility
│── requirements.txt   # Dependencies
│── README.md
```
---

## 🎯 Future Enhancements

- Real-time messaging with WebSockets

- File sharing inside rooms

- User-to-user private messaging

- Notifications & activity feed

- Role-based permissions
---

## 🤝 Contributing

Pull requests and suggestions are welcome.
Fork the project, build your feature, and submit a PR.

---

## 📜 License

This project is licensed under the **[MIT License](./LICENSE)**.  

--- 

## 👨‍💻 Author

Vinay Malyala <br> <br>
[![GitHub – VinayMalyala](https://img.shields.io/badge/GitHub-VinayMalyala-black?logo=github)](https://github.com/VinayMalyala)

---

## ⭐ Support

If you find this project useful, please ⭐ the repository to show your support!
