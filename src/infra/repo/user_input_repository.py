from collections import namedtuple
from src.infra.config import DBConnectionHandler
from src.infra.entities import UserInput

class UserInputRepository:
  """
    Class to manage User Input Repository
  """
  @classmethod
  def insert(cls, path: str, confidence: float, iou: float) -> UserInput:
    """ insert data in user input entity
    :param - path: str
           - confidence: float
           - iou: float
    :return - tuplle with new user input
    """

    InsertData = namedtuple("UserInput", "id, path, confidence, iou")

    with DBConnectionHandler() as db_connection:
      try:
        new_input = UserInput(video_path=path, confidence=confidence, iou=iou)
        db_connection.session.add(new_input)
        db_connection.session.commit()

        return InsertData(id=new_input.id, path=new_input.video_path, confidence=new_input.confidence, iou=new_input.iou)
      except:
        db_connection.session.rollback()
        raise
      finally:
        db_connection.session.close()

    return None

