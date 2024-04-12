from src.infra.config import DBConnectionHandler
from src.infra.entities import UserInput

class FakerRepo:
  @classmethod
  def insert(cls):
    
    with DBConnectionHandler() as db_connection:
      try:
          new_input = UserInput(video_path="teste", confidence=0.7, iou=0.5)
          db_connection.session.add(new_input)
          db_connection.session.commit()
      except:
         db_connection.session.rollback()
         raise
      finally:
         db_connection.session.close()