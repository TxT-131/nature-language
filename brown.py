import nltk
from nltk.corpus import brown
print('查看所有文件')
print(brown.fileids())
print('查看所有类别')
print(brown.categories())
print('查看news类别里的词')
print(brown.words(categories='news'))
print('查看类别里的句子')
print(brown.sents(categories=['news','reviews']))
