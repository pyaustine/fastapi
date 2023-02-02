from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . config import settings 


#connection to database with raw SQL
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapiPost', user='postgres', password='password123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Successful database connection")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error was, ". error)
        time.sleep(3)



#conection string
#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

#for SQLALCHEMY TO CONNECT TO POSTGRES DB
engine = create_engine(SQLALCHEMY_DATABASE_URL)


#coomunicate to DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
# Our dependency will create a new SQLAlchemy SessionLocal that will be used in a single request, and then close it once the request is finished.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
