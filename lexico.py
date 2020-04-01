import ply.lex as lex
from bs4 import BeautifulSoup
import requests
import sys
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.corpus import brown
from tokenWords import tag
from nltk.stem import PorterStemmer 

# INIT-----------
# STOPWORDS

stop_words = set(stopwords.words('english'))
dbToken = list()
userTokens = list()
ps = PorterStemmer() 

# API
title = sys.argv[1]
key = 'rwBv0LS4tFZO1J7OAzkQeg'
secret = 'LwzOepiqH4CNXOoAT7NeFEvUdv6yqPPniL97IYUFM'


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
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


# Tokenize
def stemming(input):
    stem = ''
    try:
        stem = ps.stem(input.value)
    except :
        stem = ps.stem(input)
    return stem


def tokeneize(inp):
    lexer.input(inp.lower())
    tokenList = list()
    for index in range(0, lexer.lexlen):
        try:
            tok = lexer.token()
            if tok.type != "PUNCTUATION":
                tok.type = tag(str(tok.value))
            if not tok:
                break      # No more input
            if tok.value not in stop_words:
                tok.value = stemming(tok.value)
                tokenList.append(tok)
                # print("{} : {} => Linea {}".format(
                #     str(tok.value), tok.type, str(tok.lineno)))
           
        except AttributeError:
           
            pass
    return tokenList


def get_user_tokens(input):
    for token in tokeneize(input):
        contains = findToken(token, userTokens)
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

    print(userTokens)
    return 

def get_books_tokens(input):
    for token in tokeneize(input):
        contains = findToken(token, dbToken)
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

    print(dbToken)
    return []    

def compareIndexers(indx1, indx2):
    empate = list()
    for token in indx1:
        contains = findToken(token, indx2)
        if((type(contains) != int)):
            pass
        else:
            empate.append(token)
            # print("Token empatado {}".format(token["value"]))
    return empate
def findToken(token, token_list):
    contains = False
    for (index, t) in enumerate(token_list):
        # print(index)
        # print(token.value)
        # print(t["value"])
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


def get_book_id():
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


def main():
    # Build the lexer
    lexer = lex.lex()
    id = get_book_id()
    widget = get_book_widget(id)
    reviews = get_book_reviews(widget)
    raw = BeautifulSoup(str(reviews[5]), 'xml')
    print(raw.get_text())
    # tokeneize(raw.get_text())
    get_books_tokens(raw.get_text())
    get_user_tokens(sys.argv[2])
    print(compareIndexers( dbToken, userTokens))

    print("""
    Carmen Robles
    Alberto Calleja
    Felipe Enriquez
    Mauricio Araujo
    Noe Osorio
    """)


if __name__ == "__main__":
    main()
