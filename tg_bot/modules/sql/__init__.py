from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from tg_bot import DB_URI


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

BASE = declarative_base()

def start():
    engine = create_engine("postgres://rgywlsqe:lSnciWStimBbJNt5d7EKltRLvFBmAzgA@tyke.db.elephantsql.com/rgywlsqe", client_encoding="utf8")
    BASE.metadata.bind = engine  # Make sure this line is properly indented
    return sessionmaker(bind=engine)()


BASE = declarative_base()
SESSION = start()


from sqlalchemy import create_engine


