import nltk
from nltk.corpus import webtext

for fileid in webtext.fileids():
    print(fileid)
    print(webtext.raw(fileid))
    print(len(webtext.raw(fileid)), len(webtext.words(fileid)))
    print('-----------------------------')