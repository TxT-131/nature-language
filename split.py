import re
text = ('又幻想了...幻想小日向美香是个底边...票根本卖不完，当天只有我一个人到场，蜜柑强忍着眼泪在开始公式讲话，每次看向台下只能和我对视。小游戏环节中选的也只能是我，来回上台下台主办觉得麻烦索性让我坐在了蜜柑旁边…….签名的时候staff也不赶人，我趁机多说了几句话，拿到签名板我刚想走就被蜜柑抓住了手，她求助的看着我，显然不想让我走，我只好和她继续说下去，从动画里的soyo聊到live上的蜜柑，还有她个人的发展，最后祝她能接到更多声优活，会一直支持她的。蜜柑哇的一声哭了出来，一把抱住了我，她身上妮维雅沐浴露的香气很好闻……..分别时，蜜柑还说以后MyGO每一次live都会给我一张关系者席票')
p_string = text.split('，')
print(p_string)
print('--------切分后匹配--------')
for line in p_string:
    # if re.match(pattern='蜜柑', string=line):
    #     print(line)
    if re.search(pattern = '蜜柑', string = line):
        print(line)