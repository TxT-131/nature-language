import re
import jieba
import nltk
import matplotlib.pyplot as plt
with open('./data/金庸-神雕侠侣.txt','r') as f:
    str = f.read()

cleaned_data = ''.join(re.findall('[\u4e00-\u9fa5]', str))
print('------------------使用jieba分词-----------------------')
wordlist = jieba.lcut(cleaned_data)
print('----------------------封装成text对象-----------------------')
text = nltk.Text(wordlist)
print(text)
print('--------------------找相似词-------------------------')
text.similar('小龙女',num=10)
text.concordance('侠',width=30,lines=5)
text.collocations()
print('------------绘制词汇离散图---------------')
plt.rcParams['font.sans-serif'] = ['SimHei']
words = ['小龙女','杨过','郭靖','黄蓉']
nltk.draw.dispersion.dispersion_plot(text,words,title='词汇离散表')
plt.show()