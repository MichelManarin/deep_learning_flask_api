
from src.domain.models import UserInput
from src.infra.config import DBConnectionHandler
from src.infra.entities import UserInput as UserInputModel

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

    with DBConnectionHandler() as db_connection:
      try:
        new_input = UserInputModel(video_path=path, confidence=confidence, iou=iou)
        db_connection.session.add(new_input)
        db_connection.session.commit()

        return UserInput(
          id=new_input.id, path=new_input.video_path, confidence=new_input.confidence, iou=new_input.iou
        )
      except:
        db_connection.session.rollback()
        raise
      finally:
        db_connection.session.close()

    return None

