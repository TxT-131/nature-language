import re
t = '广州:51000 深圳:51800 哈尔滨:52800 珠海:51900'
name = re.findall(r'(\D+):\d+ ?', t)
print(name)
mail = re.findall(r':(\d+)', t)
print(mail)
for data in zip(name,mail):
    print(data)

t2 = '<meta name="description" content="京东JD.COM专业...购物体验!">'
content = re.findall(r'content="(.*)"', t2)
print(content)