import nltk
from nltk.book import *
from nltk.corpus import PlaintextCorpusReader
from collections import Counter

wordlists = PlaintextCorpusReader(root='./data',fileids='.*')
print(wordlists.fileids())

with open('./data/金庸-飞狐外传.txt','r')as f:
    str = f.read()
print(len(str))
print(len(str)/len(set(str)))
print('统计平阿四，程灵素出现次数:')
print(str.count('平阿四'))
print(str.count('程灵素'))

print('查看部分文本:')
print(str [5000:5500])
print('前6个高频词')
fdist = FreqDist(str)
print(fdist.most_common(6))

W = Counter(str)
print('词频在0~99的词数量：',len([W for W in W.values() if W<100]))