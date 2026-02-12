# Gradebooks API

## Prerequisites

- Python 3.11+
- Poetry
- PostgreSQL database

## PostgreSQL Setup

### macOS (Homebrew)

**Install PostgreSQL**
   ```bash
   brew install postgresql@14
   ```

**Start PostgreSQL service**
   ```bash
   brew services start postgresql@14
   ```

**Create database and user**
   ```bash
   # Connect to PostgreSQL
   psql postgres
   
   # Create DB and User with access privileges
   CREATE DATABASE gradebooks;
   CREATE USER gradebooks_user WITH PASSWORD 'your_pw';
   GRANT ALL PRIVILEGES ON DATABASE gradebooks TO gradebooks_user;
   \q
   ```

## Setup

**Install dependencies**
   ```bash
   poetry install
   ```

**Create ENV**
   
   Create a `.env` file in the project root
   ```
   DB_URL=postgresql://gradebooks_user:your_password@localhost:5432/gradebooks
   JWT_SECRET=your-secret-key
   ```
   
   Replace `your_password` with the password you set in PostgreSQL setup.

**Run the application**
   ```bash
   poetry run uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`
   
   The database will be automatically initialized with test data on first run
   - Username: `jane123`  Password: `test123`
   - Username: `peter123` Password: `peter123`

## API Endpoints

**POST** `/login`
- Login with username and password
- Returns access token, refresh token, and student's courses with scores

Request body:
```json
{
  "username": "jane123",
  "password": "test123"
}
```

Response:
```json
{
  "access_token": "eyJhbGc...",
  "refresh_token": "eyJhbGc...",
  "courses": [
    {
      "course_id": 1,
      "course_code": "CS103",
      "course_name": "Intro to programming",
      "score": 93
    },
    ...
  ]
}
