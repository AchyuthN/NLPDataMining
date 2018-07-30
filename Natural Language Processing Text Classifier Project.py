# This project sets to build a text classifier that would identify the words with the maximum occurence in any eBook. This project 
# Importing necessary dependencies
import requests as rq
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize, sent_tokenize
# Importing Web data source (The Adventures of Sherlock Holmes)
url = 'https://www.gutenberg.org/files/1661/1661-h/1661-h.htm'
# Requests module requests and receives response from the URL simultaneously
request = rq.get(url)
text = request.text
print(text)
bs_text = BeautifulSoup(text)
bs_title = bs_text.title
print(bs_title)
# BeautifulSoup method get_text() parses through web based sources to derive the text.
text_bs = bs_text.get_text()
print(text_bs)
#Regular Expressions package in Python put together with Natural Language Toolkit is extremely powerful in dealing with unstructured text data
from nltk.tokenize import RegexpTokenizer
token = RegexpTokenizer('\w+')
tokenizer = token.tokenize(text_bs)
tokenizer[:10]
#Text preprocessing techniques implemented to eliminate repititions, duplicates and bias. Lowercasing of letter helps in preventing double counting of similar. An iterative statement runs through the entire text of the book to convert words to lowercase 
text_lower = []
for word in tokenizer:
    words = word.lower()
    text_lower.append(words)
print(text_lower)    
import nltk
words_remove = nltk.corpus.stopwords.words('english')
#Repititive words can actually skew the distribution disproportionately
words_remove[:10]
words_rm = []
for word in text_lower:
    if word not in words_remove:
        words_rm.append(word)
print(words_rm[:10])   
import matplotlib.pyplot as plt
distribution = nltk.FreqDist(words_rm)
distribution.plot(10)

#The following code builds a text miner that identifies the most recurring word and plots the frequency
#Although generously borrows from the preceding code, it has been adapted and scaled to ensure proper functionality when fed with any eBook from the Web
def plot_wordfreq(url):
    #Importing necessary dependencies
    import requests as rq
    from bs4 import BeautifulSoup
    from nltk.tokenize import word_tokenize, sent_tokenize
    # Requests module requests and receives response from the URL simultaneously
    request = rq.get(url)
    text = request.text
    print(text)
    bs_text = BeautifulSoup(text)
    bs_title = bs_text.title
    print(bs_title)
    # BeautifulSoup method get_text() searches through web sources to derive text
    text_bs = bs_text.get_text()
    print(text_bs)
    #Regular Expressions package in Python put together with Natural Language Toolkit is extremely powerful in dealing with unstructured text data
    from nltk.tokenize import RegexpTokenizer
    token = RegexpTokenizer('\w+')
    tokenizer = token.tokenize(text_bs)
    tokenizer[:10]
    #Text preprocessing techniques implemented to eliminate repititions, duplicates and bias. Lowercasing of letter helps in preventing double counting of similar. An iterative statement runs through the entire text of the book to convert words to lowercase 
    text_lower = []
    for word in tokenizer:
        words = word.lower()
        text_lower.append(words)
    print(text_lower)
    import nltk
    words_remove = nltk.corpus.stopwords.words('english')
    #Repititive words can actually
    words_remove[:10]
    words_rm = []
    for word in text_lower:
        if word not in words_remove:
            words_rm.append(word)
    print(words_rm[:10])
    import matplotlib.pyplot as plt
    distribution = nltk.FreqDist(words_rm)
    distribution.plot(10)
plot_wordfreq('https://www.gutenberg.org/files/98/98-h/98-h.htm')    
    
    