import wxpy
import os
from My_First_Web.settings import STATICFILES_DIRS

BOT = None

def login():
    path = os.path.join("%s/img" % STATICFILES_DIRS)
    if not path:
        os.makedirs(path, exist_ok=True)
    bot = wxpy.Bot(cache_path=True)
    global BOT
    BOT =bot
    return True
def get_friend(str):
    # bot = wxpy.Bot(cache_path=True)
    login()
    bot = wxpy.Bot(cache_path=True)
    # if bot:
    friends = bot.friends(update=True)
    if str in ["city","province"]:
        data = friends.stats()[str]
        key = []
        value = []
        data = sorted(data.items(),key=lambda x:x[1],reverse=True)
        for k in data[0:10]:
            if k[0] != "":
                key.append(k[0])
                value.append(k[1])
        return key,value
    elif str == "sex":
        data = friends.stats()[str]
        return data
    else:
        return [],[]
    # else:
    #     raise Exception("您未登陆！")

def logout():
    global BOT
    BOT = wxpy.Bot.logout()