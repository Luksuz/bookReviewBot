from flask import Flask
from flask_cors import CORS
from gpt import create_book_review
from service import send_bot_review_request, get_bot_posts, generate_comment

app = Flask(__name__)
CORS(app)

@app.route('/create_book_review', methods=['POST'])
def write_book_review():
    review = create_book_review()
    send_bot_review_request(review)
    return review

@app.route('/get_posts_generate_comment', methods=['POST'])
def get_posts_generate_comment():
    reviews = get_bot_posts().json()
    print(reviews)
    return generate_comment(reviews)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)