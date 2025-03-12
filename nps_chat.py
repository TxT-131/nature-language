import nltk
from nltk.corpus import nps_chat
print(nps_chat.fileids())
chatroom1 = nps_chat.posts("10-19-20s_706posts.xml")
chatroom2 = nps_chat.posts("11-09-20s_706posts.xml")
print(chatroom1)
print(chatroom2)
