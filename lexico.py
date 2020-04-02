import ply.lex as lex
import re
import json
from bs4 import BeautifulSoup

import requests
import sys
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.corpus import brown
from tokenWords import tag
from nltk.stem import PorterStemmer
from api import *
from textTest import test

# INIT-----------
# STOPWORDS

stop_words = set(stopwords.words('english'))


ps = PorterStemmer()

# API
# title = sys.argv[1]
key = 'rwBv0LS4tFZO1J7OAzkQeg'
secret = 'LwzOepiqH4CNXOoAT7NeFEvUdv6yqPPniL97IYUFM'
# db = firestore.Client()

tokens = ['WORD', "PUNCTUATION", "DIGIT", 'NUMBER', "LETTER"]

reservadas = {
    'begin': 'BEGIN'
}

t_WORD = r'[a-zA-Z]'
t_DIGIT = r'\d'
t_PUNCTUATION = r'\W'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_LETTER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.upper() in reservadas:
        t_value = t.value.upper()
        t.type = t.value
    return t

# Define a rule so we can track line numbers


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule


def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


# Tokenize
def stemming(input):
    stem = ''
    try:
        stem = ps.stem(input.value)
    except:
        stem = ps.stem(input)
    return stem


def tokeneize(inp):
    lexer.input(inp.lower())
    tokenList = list()
    for index in range(0, lexer.lexlen):
        try:
            tok = lexer.token()
            if not tok:
                break      # No more input
            if tok.type != "PUNCTUATION":
                tok.type = tag(str(tok.value))
                if tok.value not in stop_words:
                    tok.value = stemming(tok.value)
                    tokenList.append(tok)
                    # print("{} : {} => Linea {}".format(
                    #     str(tok.value), tok.type, str(tok.lineno)))

        except AttributeError:

            pass
    return tokenList


def get_user_tokens(input, log = False):
    userTokens = list()
    for token in tokeneize(input):
        contains = find_token(token, userTokens)
        if((type(contains) != int)):
            userTokens.append({
                "value": token.value,
                "count": 1,
                "type": token.type,
                "page": token.lineno,
            })
        else:
            try:
                # print("Ya estaba")
                # print(userTokens[contains])
                userTokens[contains]["count"] += 1
                pass
            except ValueError:
                print("No exite, no hay")
                pass

    if(log):
        print("\nIndexador del input de usuario:")
        for word in userTokens:
            print(word)
        print("\n")
    return userTokens


def get_books_tokens(input, log= False):
    # print(input)
    dbToken = list()
    # print(tokeneize(input))
    for token in tokeneize(input):

        contains = find_token(token, dbToken)
        if((type(contains) != int)):
            dbToken.append({
                "value": token.value,
                "count": 1,
                "type": token.type,
                "page": token.lineno,
            })
        else:
            try:
                # print("Ya estaba")
                # print(dbToken[contains])
                dbToken[contains]["count"] += 1
                pass
            except ValueError:
                print("No exite, no hay")
                pass
    if(log):
        print("\nIndexador del texto:")
        print(dbToken)
        print("\n")
    return dbToken


# def get_book_indexer(lista):
#     dbToken = list()
#     for token in tokeneize(lista):
#         contains = find_token(token, dbToken)
#         if((type(contains) != int)):
#             dbToken.append({
#                 "value": token.value,
#                 "count": 1,
#                 "type": token.type,
#                 "page": token.lineno,
#                 "books": []
#             })
#         else:
#             try:
#                 # print("Ya estaba")
#                 # print(dbToken[contains])
#                 dbToken[contains]["count"] += 1
#                 pass
#             except ValueError:
#                 print("No exite, no hay")
#                 pass

#     # print(dbToken)
#     return dbToken


def compareIndexers(indx1, indx2):
    empate = list()
    for token in indx1:
        contains = find_token(token, indx2)
        if((type(contains) != int)):
            pass
        else:
            empate.append(token)
            # print("Token empatado {}".format(token["value"]))
    return empate


def find_token(token, token_list):
    contains = False
    for (index, t) in enumerate(token_list):
        try:
            if(token.value == t["value"]):
                # print("Contiene")
                contains = index
                break
        except AttributeError:
            if(token["value"] == t["value"]):
                # print("Contiene")
                contains = index
                break
    # print(contains)
    return contains


def get_book_id(title):
    r = requests.get(
        f'https://www.goodreads.com/book/title.xml?key={key}&title={title}')
    soup = BeautifulSoup(r.text, 'xml')
    id = soup.book.id.contents[0]
    return id


def get_book_widget(id):
    r = requests.get(f'https://www.goodreads.com/book/show/{id}.xml?key={key}')
    soup = BeautifulSoup(r.text, 'xml')
    review_widget = BeautifulSoup(soup.book.reviews_widget.contents[0], 'lxml')
    return review_widget


def get_book_reviews(review_widget):
    r = requests.get(review_widget.iframe['src'])
    soup = BeautifulSoup(r.text, 'xml')
    reviews = soup.find_all('div', class_='gr_review_text')
    return reviews

def sortBook(book):
    return book["count"]

def add_indexed_books(new_books, books):

    
    for new_book in new_books:
        contains_book = -1
        for (current_id, current_book) in enumerate(books):
            if(new_book["title"] == current_book["title"]):
                contains_book = current_id
                books[current_id]["count"] += new_book["count"]
            else:
                pass    
        if(contains_book == -1):
            books.append(new_book)
    return books

def get_books_from_indexer(user_tokens, indexer):
    books = list()
    # user_token is type:
    #
    # {"value": "palabra",
    # "count": 1,
    # "type": "ADV",
    # "page": 3,}
    #
    # word_token is type:
    # 
    # 'word': word,
    # 'books': [{
    #     'title': book["title"],
    #     'genre': book["genre"],
    #     'count': 1
    # }]
    # 

    for user_token in user_tokens:
        for word_index in indexer:
            if(user_token["value"] == word_index["word"]):
                books = add_indexed_books(word_index["books"], books)
    return books

def add_to_indexer(word, book, indexer):
    contains_word = -1
    for (token_index, token) in enumerate(indexer):

        try:
            if(token["word"] == word):
                contains_word = token_index
                contains_book = -1
                for (index, token_book) in enumerate(token["books"]):
                    if(token_book["title"] == book["title"]):
                        # Ya existia
                        contains_book = index
                        indexer[token_index]["books"][index]["count"] += 1
                        # indexer[index] += 1
                    else:
                        pass
                if(contains_book == -1):
                    # print("Se agrego libro: {} -> {}".format(book["title"], word))
                    indexer[token_index]["books"].append({
                        'title': book["title"],
                        'genre': book["genre"],
                        'count': 1
                    })
            else:
                pass
        except TypeError as error:

            print(error)
            pass
    if(contains_word == -1):
        indexer.append({
            'word': word,
            'books': [{
                'title': book["title"],
                'genre': book["genre"],
                'count': 1
            }]
        })

    return indexer


def build_book_indexer():
    indexer = list()
    # {'word' : "bla", books : [
    #   {
    #       'title' : "harry potter",
    #       'count' : 6
    #   },
    #   {
    #       'title' : "hunger games",
    #       'count' : 8
    #   }
    # ]}
    docs = get_docs()
    for doc in docs:
        book = doc.to_dict()
        for i in range(0, book["tokenListCount"]):
            try:
                if(book[str(i)]):
                    for word in book[str(i)]:
                        if(word):
                            try:
                                indexer = add_to_indexer(word["value"],
                                                         {'title': book["title"], 'genre': book["genre"]}, indexer)
                            except ValueError as value_error:
                                print(value_error)
                                pass

            except KeyError:
                pass
    # print(indexer)
    return indexer


def upload_book_tokens(file_name):
    with open('{}.json'.format(file_name)) as json_data:
        data = json.load(json_data)

        for genre, books in data.items():
            for book in books:
                reviews_token_list = list()
                # print(genre, book)
                id = get_book_id(book)
                widget = get_book_widget(id)
                reviews = get_book_reviews(widget)
                # ref = db.collection('books').add({
                #     'genre': genre,
                #     'title': book,
                # })
                for review in reviews:
                    raw = BeautifulSoup(str(review), 'xml')
                    dbTokens = get_books_tokens(raw.get_text())
                    reviews_token_list.append(dbTokens)

                # print(book)
                # print(reviews_token_list)
                # print("")
                add_tokens({'genre': genre,
                            'title': book,
                            'tokenListCount': len(reviews_token_list)
                            },
                           reviews_token_list)

def print_books(books):
    for book in books:
        print("{} <<{}>> : {}".format(book["title"], book["genre"], book["count"]))

def main():
    # Build the lexer
    lexer = lex.lex()
    if(len(sys.argv) > 2):
        userTokens = get_user_tokens(sys.argv[1], log= True)
        indexer = get_books_tokens(test, log = True)
        print(compareIndexers(userTokens, indexer))

    else:
        # If you need to upload some data, uncomment line below
        # upload_book_tokens("most")
        # upload_book_tokens("10most") #Este va a tardar mucho porque son muchos libros que tiene que subir
        # First we build our indexer from DB
        indexer = build_book_indexer()
        print("Indexer ready")
        # Then we process the input from user and make it a token array
        userTokens = get_user_tokens(sys.argv[1])
        print("Input analyzed")
        # Finally we just search for each user token on aour indexer
        # we return a list of books that fits better for user
        # (that contains more words the user said)

        books = get_books_from_indexer(userTokens, indexer)
        books.sort(key = sortBook, reverse = True)
        print("Books")
        print_books(books)

    print("""
    Carmen Robles
    Alberto Calleja
    Felipe Enriquez
    Mauricio Araujo
    Noe Osorio
    """)


if __name__ == "__main__":
    main()
