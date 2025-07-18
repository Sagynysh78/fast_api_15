import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from main import app, get_session

TEST_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Синхронный движок для тестов с TestClient
engine_test = create_engine(TEST_DATABASE_URL)
SessionTest = sessionmaker(bind=engine_test, autocommit=False, autoflush=False)

@pytest.fixture(scope="session", autouse=True)
def setup_test_db():
    SQLModel.metadata.create_all(engine_test)
    yield
    SQLModel.metadata.drop_all(engine_test)

@pytest.fixture()
def client():
    def override_get_session():
        with SessionTest() as session:
            yield session
    app.dependency_overrides[get_session] = override_get_session
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear() 