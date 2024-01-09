from pyrogram import Client, filters
from config import API_ID, API_HASH, TOKEN, SESSION, MONGO_URI, HELP_PIC, ALIVE_PIC, HANDLER, BIO, BLACKLIST_CHAT, LOGGER_ID
import time

startTime = time.time()

if not API_ID:
    print("ᴀᴘɪ_ɪᴅ ɴᴏᴛ ꜰᴏᴜɴᴅ..!! 🍷 ")
    sys.exit()

if not API_HASH:
    print("ᴀᴘɪ_ʜᴀꜱʜ ɴᴏᴛ ꜰᴏᴜɴᴅ..!! 🍷")
    sys.exit()

if not SESSION:
    print("ꜱᴇꜱꜱɪᴏɴ ɴᴏᴛ ꜰᴏᴜɴᴅ..!! 🍷")
    sys.exit()

if not TOKEN:
    print("ʙᴏᴛ_ᴛᴏᴋᴇɴ ɴᴏᴛ ꜰᴏᴜɴᴅ..!! 🍷")
    sys.exit()

if not MONGO_URI:
    print("ᴍᴏɴɢᴏ_ᴜʀʟ ɴᴏᴛ ꜰᴏᴜɴᴅ..!! 🍷")
    sys.exit()

if not LOGGER_ID:
    print("ʟᴏɢɢᴇʀ_ɪᴅ ɴᴏᴛ ꜰᴏᴜɴᴅ..!! 🍷")
    sys.exit()

Bot = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
    in_memory=True,
)

Ubot = Client(name="ʀᴀꜰᴛᴀʀ 🌪", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

API_ID = API_ID
API_HASH = API_HASH
SESSION = SESSION 
TOKEN = TOKEN
MONGO_URI = MONGO_URI
LOGGER_ID = LOGGER_ID
HANDLER = HANDLER
HELP_PIC = HELP_PIC
ALIVE_PIC = ALIVE_PIC
BIO = BIO
BLACKLIST_CHAT = BLACKLIST_CHAT

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

def get_uptime(x):
    z = get_readable_time(int(x-startTime))
    return z

grt = get_readable_time
