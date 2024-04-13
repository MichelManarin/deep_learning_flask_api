from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
  """ PostgreSQL database connection """

  def __init__(self):
    self.__connection_string = "postgresql://postgres:dTfOaZxTrRfgjoyGxCuMmJLJtpDYyALa@monorail.proxy.rlwy.net:17406/railway"
    self.session = None

  def get_engine(self):
    """Return connection Engine
    :param - None
    :return - engine connection to Database
    """
    engine = create_engine(self.__connection_string)
    return engine
  
  def __enter__(self):
    engine = create_engine(self.__connection_string)
    session_maker = sessionmaker()
    self.session = session_maker(bind=engine)
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.session.close()
