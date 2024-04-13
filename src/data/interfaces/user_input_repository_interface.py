from abc import ABC, abstractmethod
from typing import List
from src.domain.models import UserInput

class UserInputRepositoryInterface(ABC):
  """ Interface to User Input Repository """

  @abstractmethod
  def insert(self, path: str, confidence: float, iou: float) -> UserInput:
    """ abstractmethod """

    raise Exception("Method not implemented")
    
  
  @abstractmethod
  def select(self, user_input_id: int = None) -> List[UserInput]:
    """ abstractmethod """

    raise Exception("Method not implemented")