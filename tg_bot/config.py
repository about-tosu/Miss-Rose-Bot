

# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "7628114935:AAEgyIkI0PM5M2fYWnfdUnhY0aktwh1Er8E"
    OWNER_ID = "6848223695" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "its_damiann"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://rgywlsqe:lSnciWStimBbJNt5d7EKltRLvFBmAzgA@tyke.db.elephantsql.com/rgywlsqe'  # needed for any database modules
    MESSAGE_DUMP = -1002318902811  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = [6606591031]  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = [5350261891]  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
