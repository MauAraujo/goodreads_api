import ply.lex as lex
from bs4 import BeautifulSoup
import requests
import sys
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.corpus import brown

from tokenWords import tag

# STOPWORDS

stop_words = set(stopwords.words('english'))

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




# Give the lexer some input
# lexer.input(data)
# lexer.input(file.read())

# Tokenize


def tokeneize(inp):
    # file = open("ejemplo.txt", "r")
    # lexer.input(file.read())
    lexer.input(inp.lower())
    while True:
        tok = lexer.token()
        try:
            if tok.type != "PUNCTUATION":
                tok.type = tag(str(tok.value))
            if not tok:
                break      # No more input
            if tok.value not in stop_words:
                print(str(tok.value) + " \t\t: " + tok.type + " \t\tLinea: " + str(tok.lineno))  
            # else:
                # print(str(tok.value) + " \t\t: " + "STOPWORD" + " \t\tLinea: " + str(tok.lineno))
        except AttributeError:
            # print("Error en atributo de {} : {}".format(tok.value, tok.type))
            pass
        
    # file.close()


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
    tokeneize(raw.get_text())
    print("""
    Carmen Robles
    Alberto Calleja
    Felipe Enriquez
    Mauricio Araujo
    Noe Osorio
    """)
    # brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
    # data = nltk.ConditionalFreqDist((word.lower(), tag))
    # tags = [tag for (tag, _) in data[word].most_common()]
    # print(word, ' '.join(tags))


if __name__ == "__main__":
    main()
