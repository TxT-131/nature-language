import jieba
# 读取文件
def jieba_high():
    corpus = []
    path = 'data/flightnews.txt'
    content = ''
    for line in open(path,'r',encoding='utf-8'):
        line = line.strip()
        content += line
    corpus.append(content)
    print('读到的内容：',corpus)
# 加载停用词，并分词

    stop_word = []
    path = 'data/stopword.txt'
    for line in open(path,'r',encoding='utf-8'):
        line = line.strip()
        stop_word.append(line)
    print('读取到的停止词',stop_word)

    split_words = []
    word_list = jieba.cut(corpus[0])
    for word in word_list:
        if word not in stop_word:
            split_words.append(word)
    print('jieba分好词:',split_words)
# 提取前十高频词
    dic = {}
    word_num = 10
    for word in split_words:
        dic[word] = dic.get(word, 0) + 1
    freq = sorted(dic.items(), key=lambda x: x[1], reverse=True)[:word_num]
    print('样本前10个高频词：' + str(freq))

jieba_high()