
from flask import Flask, request, jsonify
from lexico import *
from flask_cors import CORS


def create_app(enviroment):
    app = Flask(__name__)
    return app


app = create_app("dev")
CORS(app)

@app.route("/api/books/recomendations", methods=["POST"])
def get_recommendations():
    indexer = build_book_indexer()
    print("Indexer ready")
    # Then we process the input from user and make it a token array
    userTokens = get_user_tokens(request.json["user_input"], log=True)
    print("Input analyzed")
    # Finally we just search for each user token on aour indexer
    # we return a list of books that fits better for user
    # (that contains more words the user said)

    books = get_books_from_indexer(userTokens, indexer)
    books.sort(key=sortBook, reverse=True)
    print("Books")
    if len(books) > 5:
       books = books[:5]

    print_books(books)


    return jsonify(books)


if __name__ == '__main__':

    app.run(debug=True)
