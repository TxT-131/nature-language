import jieba

text = "月之森女子学园高中一年级学生，在吹奏乐部司职低音提琴，并先后担任过乐队CRYCHIC和MyGO!!!!!的贝斯手。CRYCHIC时期使用指弹，MyGO!!!!!时期使用拨片。"
seg_list = jieba.cut(text, cut_all=False)  # cut_all=False 表示精确模式
print("/ ".join(seg_list))