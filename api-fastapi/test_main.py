from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_todo():
    response = client.post(
        "/api/todos",
        json={"text": "Test todo", "completed": False}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Test todo"
    assert data["completed"] == False
    assert "id" in data

def test_read_todos():
    response = client.get("/api/todos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_update_todo():
    # First, create a todo
    create_response = client.post(
        "/api/todos",
        json={"text": "Update me", "completed": False}
    )
    todo_id = create_response.json()["id"]

    # Then, update it
    update_response = client.patch(
        f"/api/todos/{todo_id}",
        json={"text": "Updated todo", "completed": True}
    )
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["text"] == "Updated todo"
    assert data["completed"] == True

def test_delete_todo():
    # First, create a todo
    create_response = client.post(
        "/api/todos",
        json={"text": "Delete me", "completed": False}
    )
    todo_id = create_response.json()["id"]

    # Then, delete it
    delete_response = client.delete(f"/api/todos/{todo_id}")
    assert delete_response.status_code == 200

    # Verify it's deleted
    get_response = client.get("/api/todos")
    assert todo_id not in [todo["id"] for todo in get_response.json()]