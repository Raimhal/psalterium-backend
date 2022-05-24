from fastapi.testclient import TestClient
import main
client = TestClient(main.app)

token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbkBib29rc3RvcmUuY29tIiwicm9sZSI6IkFkbWluIiwiZXhwIjoxNjQzNzQ1MjM3fQ.QrF00BIl-so-_lMFgP3CBzIqH9zzBlq9i1FlPgbgUb8'

def test_get_book():
    response = client.get("/api/catalog/books", params={'query' : 'name', 'reverse' : False, 'skip' : 0, 'limit' : 10, 'genre' : 'all'})
    assert response.status_code == 200


def test_create_book():
    response = client.post(
        "/api/catalog/books",
        headers={'Authorization': token},
        json={
          "name": "string",
          "author": "string",
          "content": "string",
          "price": 0,
          "count": 0,
          "publication_date": "2022-01-31T19:54:00.434Z",
          "ISBN": "string1"
        }
    )
    assert response.status_code == 200

def test_delete_book():
    response = client.delete(
        "/api/catalog/books/18/delete",
        headers={'Authorization': token})
    assert response.status_code == 204

def test_update_book():
    response = client.put(
        "/api/catalog/books/18/update",
        headers={'Authorization': token},
        json={
          "name": "string",
          "author": "string",
          "content": "string",
          "price": 0,
          "count": 0,
          "publication_date": "2022-01-31T19:54:00.434Z",
          "ISBN": "1234242211435"
        })
    assert response.status_code == 404

def test_set_genres():
    response = client.patch(
        "/api/catalog/books/15/set_genres",
        headers={'Authorization': token},
        json=[
                {
                    "name" : "Fantasy"
                },
                {
                    "name" : "Romance"
                }
            ])
    assert response.status_code == 204