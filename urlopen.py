import nltk
from urllib.request import urlopen
html1 = urlopen('https://www.gutenberg.org/cache/epub/25352/pg25352-images.html').read()
html1 = html1.decode('utf8')
print(html1)