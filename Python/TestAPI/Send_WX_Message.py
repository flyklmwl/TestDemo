from wxpy import *


#bot = Bot()
bot = Bot(console_qr=2,cache_path="botoo.pkl")
my_friend = bot.friends().search(u'�ǳ�')[0]
my_friend.send('Hello WeChat!')

# linuxִ�е�½�������������