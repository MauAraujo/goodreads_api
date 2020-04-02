import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

array = [{'value': 'lot', 'count': 2, 'type': 'NOUN', 'page': 3}, {'value': 'thing', 'count': 2, 'type': 'NOUN', 'page': 3}, {'value': 'troubl', 'count': 1, 'type': 'VERB', 'page': 3}, {'value': 'hunger', 'count': 1, 'type': 'NOUN', 'page': 3}, {'value': 'game', 'count': 1, 'type': 'NOUN', 'page': 3}, {'value': '.', 'count': 8, 'type': 'PUNCTUATION', 'page': 3}, {'value': 'perceiv', 'count': 1, 'type': 'NOUN', 'page': 3}, {'value': 'sole', 'count': 1, 'type': 'ADV', 'page': 3}, {'value': 'connect', 'count': 1, 'type': 'VERB', 'page': 3}, {'value': 'book', 'count': 1, 'type': 'NOUN', 'page': 3}, {'value': 'metaphor', 'count': 1, 'type': 'NOUN', 'page': 3}, {
    'value': 'behind', 'count': 1, 'type': 'ADP', 'page': 3}, {'value': 'word', 'count': 1, 'type': 'NOUN', 'page': 3}, {'value': 'peopl', 'count': 1, 'type': 'NOUN', 'page': 3}, {'value': 'attach', 'count': 1, 'type': 'NOUN', 'page': 3}, {'value': 'fiction', 'count': 1, 'type': 'ADJ', 'page': 3}, {'value': 'freedom', 'count': 1, 'type': 'NOUN', 'page': 3}, {'value': 'without', 'count': 1, 'type': 'ADP', 'page': 3}, {'value': 'see', 'count': 1, 'type': 'VERB', 'page': 3}, {'value': 'realli', 'count': 1, 'type': 'ADV', 'page': 3}, {'value': 'someth', 'count': 1, 'type': 'NOUN', 'page': 3}, {'value': 'unfortu', 'count': 1, 'type': 'NOUN', 'page': 3}]
array2 = [{'value': 'behind', 'count': 1, 'type': 'ADP', 'page': 4}, {'value': 'word', 'count': 1, 'type': 'NOUN', 'page': 4}, {'value': '.', 'count': 1,
                                                                                                                                'type': 'PUNCTUATION', 'page': 4}, {'value': 'peopl', 'count': 1, 'type': 'NOUN', 'page': 4}, {'value': 'attach', 'count': 1, 'type': 'NOUN', 'page': 4}]
[{'value': '.', 'count': 8, 'type': 'PUNCTUATION', 'page': 3}, {'value': 'behind', 'count': 1, 'type': 'ADP', 'page': 3}, {'value': 'word', 'count': 1,
                                                                                                                           'type': 'NOUN', 'page': 3}, {'value': 'peopl', 'count': 1, 'type': 'NOUN', 'page': 3}, {'value': 'attach', 'count': 1, 'type': 'NOUN', 'page': 3}]
# Read


def addToken(book, tokenLists):
    doc_ref = db.collection(u'tokens').document()
    doc_ref.set(
        {"book": book["name"], "tokenListCount": len(tokenLists)}, merge=True)
    for (index, tokenList) in enumerate(tokenLists):
        doc_ref.set({str(index): tokenList}, merge=True)


def readTokens():
    users_ref = db.collection(u'tokens')
    docs = users_ref.stream()
    tokens = list()

    for doc in docs:
        data = doc.to_dict()

        print(data["book"])
        for i in range(0, data["tokenListCount"]):
            if(data[str(i)]):
                for token in data[str(i)]:
                    tokens.append(token)
        print(tokens)
        print(u'{} => {}'.format(doc.id, data["book"]))
    

def concat(arr1, arr2):
    for element in arr2:
        arr1.append(element)


def main():
    addToken([array, array2])
    readTokens()


if __name__ == "__main__":
    main()
