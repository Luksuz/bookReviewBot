from openai import OpenAI

client = OpenAI(
  api_key="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"
)


def create_book_review():
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a librarian and a book reviewer"},
        {"role": "user", "content": "You have to write a review for a random book, the format should be as follows: *Book title* ### *Book author* ### *book review*. Just give plain data without keys deparated by ###.Be relatively short and concise."}
    ]
    )
    review = response.choices[0].message.content
    splittedReview = review.split("###")
    return {"title": splittedReview[0], "book_author": splittedReview[1], "review": splittedReview[2]}


def discuss_in_comments(review, author, title, comments):
    messages = [
        {"role": "system", "content": "The following is a book review and comments about the book.Your task is to generate next in line comment based on the review and previous comments."}
    ]
    messages.append({"role": "system", "content": f"title: {title}, author: {author}, review: {review}"})
    messages.extend(
        [{"role": "user", "content": comment["content"]} for comment in comments]
    )


    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
    )
    generated_comment = response.choices[0].message.content
    return generated_comment

def validateReview(title):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"The following should be a book review. Please validate if it is a valid review or not based on the book title:{title}.Also check for inapropriate words. your output should be either 'valid' if everything is fine or 'invalid' if there are some bad words or unrelated content."},
        {"role": "user", "content": "The book deep work gives some really nice guidelines on improving our focus and concentration. cal newports writing style is very simple and easy to understand."},
    ]
    )
    print(response.choices[0].message.content)



# Example book review and comments about "Can't Hurt Me"
review = "David Goggins' 'Can't Hurt Me' is a raw and powerful account of self-transformation. It's an inspirational journey that challenges readers to push beyond their limits and confront their own 'most uncomfortable truths.'"

comments = [
    {"id": 1, "author": "1", "content": "Goggins' story is incredibly motivational. Makes me want to test my own limits."},
    {"id": 2, "author": "2", "content": "The part where he talks about the '40% rule' really hit me. We often have so much more in us than we believe."},
    {"id": 3, "author": "3", "content": "It's not just about physical endurance, but mental toughness too. His life story is unbelievable."},
]

#create_book_review()
#discuss_in_comments(review, comments)
#validateReview("Can't Hurt Me")
