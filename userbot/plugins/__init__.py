import datetime
from vampbot.config import Config
from vampbot.helpers import *
from vampbot.utils import *
from vampbot.random_strings import *
from vampbot.version import __vamp__
from telethon import version


VAMP_USER = bot.me.first_name
D15H4NT0P = bot.uid
vamp_mention = f"[{VAMP_USER}](tg://user?id={D15H4NT0P})"
vamp_logo = "./vampbot/resources/pics/vampbot_logo.jpg"
cjb = "./vampbot/resources/pics/cjb.jpg"
restlo = "./vampbot/resources/pics/rest.jpeg"
shuru = "./vampbot/resources/pics/shuru.jpg"
shhh = "./vampbot/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
vamp_ver = __vamp__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"

START_TIME = datetime.datetime.now()
uptime = f"{str(datetime.datetime.now() - START_TIME).split('.')[0]}"
my_channel = Config.MY_CHANNEL or "VAMPBOT_OFFICIAL"
my_group = Config.MY_GROUP or "VAMPBOT_SUPPORT"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/VampBot_Official"
vamp_channel = f"[†hê vãmpẞø†]({chnl_link})"
grp_link = "https://t.me/VampBot_Support"
vamp_grp = f"[vãmpẞø† Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# vampbot
