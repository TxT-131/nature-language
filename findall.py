import re
text = ('我是蜜蜜柑噶，我又幻想了...幻想小日向美香是个底边...票根本卖不完，当天只有我一个人到场，蜜柑强忍着眼泪在开始公式讲话，每次看向台下只能和我对视。小游戏环节中选的也只能是我，来回上台下台主办觉得麻烦索性让我坐在了蜜柑旁边…….签名的时候staff也不赶人，我趁机多说了几句话，拿到签名板我刚想走就被蜜柑抓住了手，她求助的看着我，显然不想让我走，我只好和她继续说下去，从动画里的soyo聊到live上的蜜柑，还有她个人的发展，最后祝她能接到更多声优活，会一直支持她的。蜜柑哇的一声哭了出来，一把抱住了我，她身上妮维雅沐浴露的香气很好闻……..分别时，蜜柑还说以后MyGO每一次live都会给我一张关系者席票')
# result = re.findall(pattern='蜜柑',string=text)
# result0 = re.findall(pattern='蜜柑.',string=text)
# result1 = re.findall(pattern='蜜柑[噶强]',string=text)
# result2 = re.findall(pattern='..yo',string=text)
# result3 = re.findall(pattern='[o]yo',string=text)
# result4 = re.findall(pattern='蜜柑|soyo',string=text)
# print(result0)
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# for line in text.split('，'):
#     if len(re.findall(pattern='蜜柑|soyo',string=text)):
#         print(line)

# result5 = re.findall(pattern='蜜柑|soyo',string=text)
# print(result5)
# for line in text.split('，'):
#     if len(re.findall(pattern='^蜜柑',string=line)):
#         print(line)
# for line in text.split('，'):
#     if len(re.findall(pattern='蜜柑$',string=line)):
#         print(line)

# 量化符号要一个字
result6 = re.findall(pattern='柑', string=text)
print(result6)
result7 = re.findall(pattern='柑?', string=text)
print(result7)
result8 = re.findall(pattern='柑*', string=text)
print(result8)
result9 = re.findall(pattern='柑+', string=text)
print(result9)
result10 = re.findall(pattern='蜜{1}',string=text)
print(result10)
result11 = re.findall(pattern='蜜{2}',string=text)
print(result11)
result12 = re.findall(pattern='蜜{1,2}',string=text)
print(result12)
result13 =re.findall(pattern='s.+',string=text)
print(result13)
result14 =re.findall(pattern='s+...',string=text)
print(result14)