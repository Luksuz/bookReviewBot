import random
import requests
from gpt import create_book_review, discuss_in_comments, validateReview

def send_bot_review_request(review):
    random_bot_id = random.randint(1, 909)

    requests.post(f"http://localhost:8000/api/create_bot/{random_bot_id}", data=review)

def get_bot_posts():
    random_bot_id = random.randint(1, 909)
    posts = requests.get(f"http://localhost:8000/api/bot/get_other_bot_posts/{random_bot_id}")
    return posts

def generate_review():
    random_bot_id = random.randint(1, 909)
    review = create_book_review()
    review["author"] = random_bot_id
    print(review)
    posted_review = requests.post(f"http://localhost:8000/api/bot/create_review", data=review)
    return posted_review

def generate_comment(reviews):
    random_review = reviews[random.randint(0, len(reviews) - 1)]
    random_reviewer = random.randint(1, 909)
    post_id = random_review["id"]
    title = random_review["title"]
    author = random_review["author"]
    review = random_review["content"]
    comments = random_review["comments"]
    generated_comment = discuss_in_comments(review, author, title, comments)
    requests.post(f"http://localhost:8000/api/bot/comment_review", data={"title": {author}, "post": {post_id}, "author": random_reviewer, "content": generated_comment})
    return generated_comment

def follow():
    random_follower = random.randint(1, 909)
    random_bot_id = random.randint(1, 909)
    return requests.post(f"http://localhost:8000/api/bot/follow", data={"follower": random_follower, "following": random_bot_id}).json()

def like():
    random_bot_id = random.randint(1, 909)
    random_post_id = random.randint(1, 25)
    return requests.post(f"http://localhost:8000/api/bot/like_post", data={"post": random_post_id, "user": random_bot_id}).json()