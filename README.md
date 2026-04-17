# 🚀 SRN Analyst App

## 📌 Overview
Job Analyst App is a backend web application built using Flask that provides APIs for managing and analyzing organizational data. The application supports secure authentication, database operations, and structured data processing.

It is designed with a modular architecture to ensure scalability, maintainability, and ease of integration with frontend systems.

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Framework:** Flask, Flask-RESTX  
- **Database:** MySQL  
- **ORM:** SQLAlchemy  
- **Authentication:** JWT (JSON Web Tokens)  
- **Data Processing:** Pandas  
- **Migrations:** Alembic  

---

## ✨ Features
- 🔐 User authentication and authorization using JWT  
- 📡 RESTful API development  
- 🗂️ Management of organizations, proposals, and data sources  
- 🧮 Data processing with Excel/CSV files using Pandas  
- 🗃️ Database integration with MySQL  
- 🔄 Database migrations using Alembic  
- 🧩 Modular and scalable project structure  

---

## 📂 Project Structure
job-analyst-app/
│── app/
│ ├── models/ # Database models
│ ├── routes/ # API routes
│ ├── services/ # Business logic
│ ├── utils/ # Helper functions
│── migrations/ # Alembic migration files
│── config.py # Configuration settings
│── run.py # Application entry point
│── requirements.txt # Dependencies

⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/srn-analyst-app.git
cd srn-analyst-app
###2️⃣ Create virtual environment
python -m venv venv
Windows:
   venv\Scripts\activate
###3️⃣ Install dependencies
   pip install -r requirements.txt
###4️⃣ Configure environment variables
   SECRET_KEY=your_secret_key
DATABASE_URL=mysql+pymysql://username:password@localhost/db_name

###5️⃣ Run database migrations
   alembic upgrade head
###6️⃣ Run the application
    python run.py
App will run on:

http://127.0.0.1:5000/
###API Endpoints (Sample)
POST /login → User login
GET /organizations → Fetch organizations
POST /proposals → Create proposal
GET /datasources → Fetch data sources

###🔗 API Endpoints (Sample)
POST /login → User login
GET /organizations → Fetch organizations
POST /proposals → Create proposal
GET /datasources → Fetch data sources

###📊 Use Cases
Backend system for business data management
API layer for analytics dashboards
Data processing and validation system

###🚀 Future Enhancements
Add frontend UI (React/Angular)
Deploy on cloud (AWS/GCP)
Add role-based access control
Improve data analytics features

###👩‍💻 Author

Nivedita Sharma
