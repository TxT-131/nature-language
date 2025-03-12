import nltk
from nltk.corpus import reuters
print('查看类别')
print(reuters.categories())
print(len(reuters.categories()))
print('查看文件')
print(reuters.fileids()[10:15])