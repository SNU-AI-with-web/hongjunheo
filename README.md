# Example Project

React + FastAPI fullstack web application.

## Project Structure

```
  example/
  ├── backend/
  │   └── .venv/
  │   └── server.py
  │   └── requirements.txt
  ├── frontend/
  │   ├── App.jsx
  │   ├── main.jsx
  │   ├── index.html
  │   ├── package.json
  │   └── vite.config.js
  └── README.md
```

## Tech Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **Uvicorn**: ASGI server

### Frontend
- **React**: UI library
- **Vite**: Build tool and dev server
- **JavaScript/JSX**: Programming language

## Installation & Setup

### 1. Python Virtual Environment

```bash
cd backend
# Create virtual environment with uv
uv venv

# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate  # Windows
```

### 2. Install Python Dependencies

```bash
uv pip install -r requirements.txt
cd ..
```

### 3. Install Frontend Dependencies

```bash
cd frontend
npm install
cd ..
```

### 4. Run Servers

#### Backend Server (Port 8000)
```bash
cd backend
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Server (Port 5173)
```bash
cd frontend
npm run dev
```

## API Endpoints

### POST /user
Check if user is adult based on age.

**Request:**
```json
{
  "name": "John Doe",
  "age": 25
}
```

**Response:**
```json
{
  "message": "Hello John Doe!",
  "is_adult": true
}
```

## Requirements

- Python 3.13+
- Node.js 18+
- npm or yarn