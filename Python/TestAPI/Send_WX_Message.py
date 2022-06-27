from wxpy import *


#bot = Bot()
bot = Bot(console_qr=2,cache_path="botoo.pkl")
my_friend = bot.friends().search(u'昵称')[0]
my_friend.send('Hello WeChat!')

# linux执行登陆请调用下面的这句