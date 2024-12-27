from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


from sqlalchemy import create_engine

DB_URI = "postgresql://rgywlsqe:lSnciWStimBbJNt5d7EKltRLvFBmAzgA@tyke.db.elephantsql.com/rgywlsqe"
try:
    engine = create_engine(DB_URI)
    connection = engine.connect()
    print("Database connection successful!")
    connection.close()
    except Exception as e:
    print(f"Error: {e}")
BASE = declarative_base()  # Correct placement

    BASE.metadata.bind = engine  # Make sure this line is properly indented
    return sessionmaker(bind=engine)()


BASE = declarative_base()
SESSION = start()




