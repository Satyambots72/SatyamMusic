import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID","6435225"))
API_HASH = getenv("API_HASH","4e984ea35f854762dcde906dce426c2d")
BOT_TOKEN = getenv("BOT_TOKEN","6082036827:AAF4vmfVEqyhE8FZH9WYsf9Auw_fmTtU2e4")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Ishq:80IP5QTFQtvM8i5L@ishq.rwtsuig.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "99999999"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001840241140"))
OWNER_ID = int(getenv("OWNER_ID", 5097836954))
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/Satyambots72/SatyamMusic",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/satyamnetwork")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+SWooBuMdjPxkODFl")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION", "BAAtI7vxop5QaO-YozvkXtz3bYZmU-0hoHGQj64lnJ8nzITtXEkqsWS2By84SdJ3VnIBPmEwbRBUrpjZxJVU2iKuBlf2P7A-T5n1j93S2H8q0fvNTFD-8Yg-th4RY9WpzCrsAFCsKWxRrPzyJrGUlnJEoCwIVFfputvVEG9J-Cd1EAqJo8ArePIY4rjVQMiPif56tIUjrpGoZ9gsklZJ3654R6QL2eb-UIWJSDbZJX6QvgT-G4SUqm0QCMh1rwTyNqqGyLGqHAoIK3w9pCl7HX2YHULESIg54KxaPNWNloiAlyQYTaKdGQv-k62WXwS7knPJo5EoHGHNWaxxQB_bm5VKAAAAAX_cLBAA")
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
    "START_IMG_URL", "https://telegra.ph/file/f03c2fbfd5150b8e90c18.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/f03c2fbfd5150b8e90c18.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://telegra.ph/file/f03c2fbfd5150b8e90c18.jpg"
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


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


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
