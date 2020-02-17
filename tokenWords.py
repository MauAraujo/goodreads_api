import nltk 
# nltk.download()
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 
# nltk.download('stopwords')
stop_words = set(stopwords.words('english')) 
  

txt = """Sukanya, Rajib and Naba are my good friends.   
    Sukanya is getting married next year. 
    Marriage is a big step in one’s life.
    It is both exciting and frightening. " \ 
    But friendship is a sacred bond between people." \ 
    It is a special kind of love between us. " \ 
    Many of you must have tried searching for a friend "\ 
    but never found the right one."""
  
# sent_tokenize is one of instances of  
# PunktSentenceTokenizer from the nltk.tokenize.punkt module 
  
def tag(word):
    try:
        tagged = nltk.pos_tag([word], tagset="universal", lang="eng")   
        _ , y = tagged[0]
        return y
    except TypeError:
        print("Error en token de {}".format(word))
        return "NOT FOUND"    
        
    

word = "."
tagged = nltk.pos_tag([word], tagset="universal", lang="eng")   
x, y = tagged[0]
print("{} is {}".format(x,y))

# tokenized = sent_tokenize(txt) 
# for i in tokenized: 
      
#     # Word tokenizers is used to find the words  
#     # and punctuation in a string 
#     wordsList = nltk.word_tokenize(i) 
  
#     # removing stop words from wordList 
#     wordsList = [w for w in wordsList if not w in stop_words]  
  
#     #  Using a Tagger. Which is part-of-speech  
#     # tagger or POS-tagger.  
#     print("\n")
#     print(wordsList)
#     tagged = nltk.pos_tag(wordsList, tagset="universal", lang="eng") 
  
#     print(tagged) 