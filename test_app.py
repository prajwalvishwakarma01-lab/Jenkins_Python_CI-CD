from app import app

client = app.test_client()

def test_home():

    response = client.get("/")

    assert response.status_code == 200

def test_get_employees():

    response = client.get("/employees")

    assert response.status_code == 200