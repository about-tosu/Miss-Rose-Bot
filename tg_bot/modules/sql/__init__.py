from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from tg_bot import DB_URI


from sqlalchemy import create_engine

DB_URI = "postgresql://rgywlsqe:lSnciWStimBbJNt5d7EKltRLvFBmAzgA@tyke.db.elephantsql.com/rgywlsqe"
try:
    engine = create_engine(DB_URI)
    connection = engine.connect()
    print("Database connection successful!")
    connection.close()


SESSION = start()




