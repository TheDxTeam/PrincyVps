import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", 23201258))
API_HASH = getenv("API_HASH","2dbcbc118e7ef89d48dafc23c3280cfa")
BOT_TOKEN = getenv("BOT_TOKEN","6341777841:AAGcrY2XBhlP_Dh1psWYqhKasbn9rSjfDuk")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://PrincyMusicBot:Princy@cluster0.vhfri5f.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1080))
LOGGER_ID = int(getenv("LOGGER_ID", -1001853824665))
OWNER_USERNAME = getenv("OWNER_USERNAME","TheKidPersonOp")
CHAT_GROUP = getenv("CHAT_GROUP","https://t.me/FRIENDS2FAMILY00")
OWNER_ID = int(getenv("OWNER_ID", 6507819384))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/TheDxCoderteam/PrincyMusicVps",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL","https://t.me/NeoUpdatess")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FRIENDS2FAMILY00")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
AUTO_GCAST = getenv("AUTO_GCAST","True")
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")
PROMO = getenv("PROMO","https://graph.org/file/7ecd7f937fe61a540c8a7.jpg")
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

STRING1 = getenv("STRING_SESSION", "BQFiBeoAeadSoEaNUGFbKvs3JHTTKQvCxlTCV-289QrpqCy_6hawyJb2aYyOMCOsqhX470QhoOSPQIixd5bw4ZbduoNazpYwkEixaKh3KdcE6ikrq25Nb1w8jw2aiFylY431iBgAX6ydCe_sjvsz_b04InDooyxE5DnVnTQ4xtCpg4ussOpCt6hr3o6rCZ9839VfZPWqjT29g8tlm6BJFKJ8w39q1HGfJyqU90aJOFB7wR_kPcuuGA8xIekV48GjNdDoMBzfSsGrE1KZpDKe3W8airE4S76AOb0KXm45uR2fsHAS5JTaIfkAadzZijPItB_k6UUw5rXkdJFsiLdWJ-tS371K4gAAAAFaEHADAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/5ecd0f25385b52fbbc3e8.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:180"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
