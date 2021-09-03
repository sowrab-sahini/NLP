import urllib.request
from bs4 import BeautifulSoup
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

#Using urllib library to read SpaceX wikipedia page

response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html =  response.read()

#Using Beautiful Soup to parse raw html data
soup = BeautifulSoup(html, "html5lib")
text = soup.get_text(strip = True)
tokens = [t for t in text.split()]
clean_tokens = tokens[:]

#Using NLTKs Frequency Distribution to count the word frequency
frequency = nltk.FreqDist(tokens)
keys =[]
values = []

for key,val in frequency.items():
    #Printing Values whose frequency is greater than 5
    if val>5:
        print(str(key) + ':' +str(val))
        keys.append(key)
        values.append(val)
    else:
        tokens.remove(key)

#Plotting graph without removing stopwords
frequency.plot(20,cumulative= False)

#After removal of stop words
for token in tokens:
    #Removing Tokens which have digits
    if str(token).isdigit():
        clean_tokens.remove(token)
    #Removing English language Stopwords
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

#Calculating Frequency after removing stopwords
final = nltk.FreqDist(clean_tokens)

#Plotting first 10 high distribution words
final.plot(10,cumulative= False)

#Plotting Bar graph as other form of frequency visualization
plt.bar(keys[0:10], values[0:10], color='green')
plt.show()



