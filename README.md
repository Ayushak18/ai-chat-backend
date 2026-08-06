# AI Chat Backend

A production-oriented AI Chat Backend built with **FastAPI**, **SQLAlchemy**, **JWT Authentication**, and **Groq LLM**.

The project is designed as a learning-focused backend while following clean architecture principles such as Repository Pattern, Service Layer, Dependency Injection, and Separation of Concerns.

---

# Features

## Authentication

- User Registration
- User Login
- Password Hashing
- JWT Authentication
- Protected Routes

---

## Conversation Management

- Create Conversations
- Retrieve User Conversations
- Authorization Checks
- Conversation Ownership Validation

---

## Message Management

- Store User Messages
- Store AI Responses
- Retrieve Conversation Messages
- Messages Ordered Chronologically

---

## AI Chat

- Chat with an LLM using Groq
- Multi-turn Conversation Support
- Conversation History
- Clean LLM Abstraction Layer

---

## Architecture

```
Client
   │
   ▼
FastAPI Routes
   │
   ▼
Services
   │
   ▼
Repositories
   │
   ▼
SQLAlchemy
   │
   ▼
PostgreSQL / SQLite
```

LLM communication is isolated behind an `LLMService`.

```
ChatService
      │
      ▼
LLMService
      │
      ▼
Groq API
```

This makes it easy to replace Groq with another provider in the future.

---

# Tech Stack

## Backend

- Python 3.12+
- FastAPI
- SQLAlchemy
- Alembic
- Pydantic v2
- Pydantic Settings

## Authentication

- JWT
- Passlib / bcrypt

## Database

- SQLite (Development)
- PostgreSQL (Planned)

## AI

- Groq SDK
- Llama 3.3 70B Versatile

---

# Project Structure

```
app/
│
├── api/
│
├── config/
│
├── database/
│
├── dependencies/
│
├── enum/
│
├── repositories/
│
├── schemas/
│
├── services/
│
├── utils/
│
└── main.py
```

---

# Design Principles

- Repository Pattern
- Service Layer Pattern
- Dependency Injection
- Single Responsibility Principle
- Separation of Concerns

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
```

Move into the project.

```bash
cd ai-chat-backend
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the environment.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

Example:

```env
LLM_API_KEY=your_groq_api_key
LLM_MODEL=llama-3.3-70b-versatile

JWT_SECRET=your_secret
JWT_ALGORITHM=HS256
JWT_EXPIRATION_MINUTES=60

DATABASE_URL=sqlite:///./chat.db
```

> Do **not** commit your `.env` file. Use `.env.example` as a template.

---

# Database

Run migrations.

```bash
alembic upgrade head
```

---

# Running the Project

Start the development server.

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# Current API Endpoints

## Authentication

```
POST /auth/register
POST /auth/login
GET  /auth/me
```

---

## Conversations

```
GET /conversations
GET /conversations/{conversation_id}/messages
```

---

## Chat

```
POST /chat
```

Example Request:

```json
{
    "message": "Explain React reconciliation.",
    "conversation_id": null
}
```

Example Response:

```json
{
    "message": "React reconciliation is...",
    "conversation_id": 1
}
```

---

# Current Workflow

```
User
 │
 ▼
POST /chat
 │
 ▼
Create/Get Conversation
 │
 ▼
Save User Message
 │
 ▼
Retrieve Conversation History
 │
 ▼
Build LLM Messages
 │
 ▼
Groq LLM
 │
 ▼
Save Assistant Message
 │
 ▼
Return Response
```

---

# Roadmap

### Completed

- Authentication
- JWT
- Conversations
- Messages
- AI Integration
- Conversation History

### Planned

- Streaming Responses
- RAG
- Vector Database
- LangGraph
- Multi-Agent Workflows
- PDF Upload Support
- PostgreSQL
- Async SQLAlchemy
- Conversation Summarization
- Long-Term Memory

---

# Learning Objectives

This project focuses on learning production backend engineering concepts including:

- REST API Design
- FastAPI
- SQLAlchemy
- Authentication
- Repository Pattern
- Service Layer
- Dependency Injection
- AI Backend Development
- LLM Integration
- Prompt Construction
- Conversation Management

---

# Future Improvements

- Streaming AI responses
- Conversation summarization
- Token-aware context management
- Background jobs
- Rate limiting
- Logging and monitoring
- Unit and integration tests
- Docker support
- CI/CD pipeline

---

# License

This project is intended for educational purposes and backend engineering practice.
