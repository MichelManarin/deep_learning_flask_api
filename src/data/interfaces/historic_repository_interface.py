from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Historic

class HistoricRepositoryInterface(ABC):
  """ Interface to Historic Repository """

  @abstractmethod
  def select(self) -> List[Historic]:
    """ abstractmethod """

    raise Exception("Method not implemented")
    
  
  # @abstractmethod
  # def select(self, user_input_id: int = None) -> List[DetectionResult]:
  #   """ abstractmethod """

  #   raise Exception("Method not implemented")