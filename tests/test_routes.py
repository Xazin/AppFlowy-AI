import json

import pytest
from app import create_app
from app.config import TestingConfig


@pytest.fixture
def client():
    app = create_app(TestingConfig)
    with app.test_client() as client:
        yield client


def test_summarize_row(client):
    """Test the summarize row."""
    data = {"name": "Jack", "age": 25, "city": "New York"}
    response = client.post("/summarize_row", json=data)
    assert response.status_code == 200

    summary = response.get_json().get("data", "")

    # List of keywords you expect to be present in the summary
    expected_keywords = ["Jack", "25", "New York"]

    # Check if each keyword is present in the summary
    for keyword in expected_keywords:
        assert keyword in summary, f"Keyword '{keyword}' not found in summary"


def test_translate_row(client):
    """Test the summarize row."""
    data = {"name": "Jack", "age": 25, "city": "New York"}
    response = client.post("/translate_row", json=data)
    assert response.status_code == 200

    output_json = json.load(response.get_json().get("data", ""))
    expected_json = {"姓名": "杰克", "年龄": "25", "城市": "纽约"}

    # assert every key-value in expected_json is present in output_json
    for key, value in expected_json.items():
        assert key in output_json
        assert output_json[key] == value
