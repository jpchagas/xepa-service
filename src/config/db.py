
import sqlalchemy as sq

def create_connection():
    engine = sq.crecreate_engine('mysql+pymysql://dba:J10p02c9315.@localhost/xepa', echo=True)
    #Create a session
    Session = sq.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    return session