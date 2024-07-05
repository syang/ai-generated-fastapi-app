from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db/test_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)
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

def test_create_item():
    response = client.post(
        "/items/",
        json={"item_name": "Test Item", "item_price": 10.5, "expiration_date": "2024-12-31"},
    )
    assert response.status_code == 200
    assert response.json()["item_name"] == "Test Item"
    assert response.json()["item_price"] == 10.5

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
