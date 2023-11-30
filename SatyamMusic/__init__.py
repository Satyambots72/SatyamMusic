from SatyamMusic.core.bot import Anony
from SatyamMusic.core.dir import dirr
from SatyamMusic.core.git import git
from SatyamMusic.core.userbot import Userbot
from SatyamMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
