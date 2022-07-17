from fastapi.testclient import TestClient

from main import app
#from routers.items import fake_items_db

client = TestClient(app)


# def test_read_main():
#     response = client.get("/items/", headers={"X-Token": "fake-super-secret-token"}, params={"token": "jessica"})
#
#     assert response.status_code == 200
#     assert response.json() == fake_items_db

def test_true():
    assert 1 == 1
