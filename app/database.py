#connect DB
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote  
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
#from .config import setting


#SQLALCHEMY_DB_URL = 'postgresql://<username>:<passowrd>@<ipaddress/hostname>/<database_name>'

SQLALCHEMY_DB_URL = f'postgresql://{settings.database_username}:%s@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DB_URL % quote(settings.database_password))

SessionLocal = sessionmaker(autocommit =False, autoflush= False, bind =engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

<<<<<<< HEAD
 while True: 
=======
# while True: 
>>>>>>> 22a8fd8f44ed992339d7930785e594b33efef772

#     try:
#         conn=psycopg2.connect(host ='localhost', database = 'fastapi', user = 'postgres', 
#         password = 'qwer1234!@#$', cursor_factory = RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was sucessfull!")
#         break
#     except Exception as error:
#         print("Connecting to DB failed")
#         print("Error: ", error)
<<<<<<< HEAD
#         time.sleep(2)
=======
#         time.sleep(2)
>>>>>>> 22a8fd8f44ed992339d7930785e594b33efef772
