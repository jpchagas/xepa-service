from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('mysql+pymysql://dba:J10p02c9315.@localhost/xepa', echo=True)

Base.metadata.create_all(engine)
'''
Session = sessionmaker(bind=engine)
session = Session()

user = User(name='John Snow', password='johnspassword')
session.add(user)

print(user.id)  # None
'''