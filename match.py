import re
text = ('哈哈，今天植树节，在学校门口看见一群拎着水带着手套的年轻人，一定是去种树的吧')
result = re.match(pattern='哈哈',string=text)
print(result)