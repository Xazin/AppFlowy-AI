import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client


def test_summarize_row(client):
    """Test the summarize row."""
    data = {"name": "Jack", "age": 25, "city": "New York"}
    response = client.post("/summarize_row", json=data)
    assert response.status_code == 200

    text = response.get_json()["data"]["text"]
    # the text will be something like: Jack is 25 years old and lives in New
    # York
    assert text != ""


def test_translate_row(client):
    """Test the summarize row."""
    data = {"name": "Jack", "age": 25, "city": "New York"}
    response = client.post("/translate_row", json=data)
    assert response.status_code == 200

    output_json = response.get_json()["data"]["text"]
    expected_json = {"姓名": "杰克", "年龄": "25", "城市": "纽约"}

    # assert every key-value in expected_json is present in output_json
    for key, value in expected_json.items():
        assert key in output_json
        assert output_json[key] == value
