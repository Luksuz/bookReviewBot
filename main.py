from flask import Flask
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/create_accounts', methods=['POST'])
def create_accounts():
    response = requests.post('http://localhost:8000/api/register/', json={
        'username': 'test',
        'password': 'test',
        'email': 'NDN@dnj.ccm'
    })
    return response.json()

@app.route('/write_book_review', methods=['POST'])
def write_book_review():
    token = requests.post('http://localhost:8000/api/login/', json={
        "username": "test",
        "password": "test"
    }).json()['token']
    print(token)
    """response = requests.post('http://localhost:8000/api/reviews/',
                             headers={
                                "Authorization": f"Token {token}"
                             },
                             json={
        'book': "Winnie the Pooh",
        'content': 'This is a test review This is a test reviewThis is a test review This is a test reviewvThis is a test review',
    })"""

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)