from abc import ABC, abstractmethod
from typing import List
from src.domain.models import DetectionResult

class DetectionResultsRepositoryInterface(ABC):
  """ Interface to DetectionResults Repository """

  @abstractmethod
  def insert(self, user_input_id: int, number_fps: int, confidence: float, image_base64: str) -> DetectionResult:
    """ abstractmethod """

    raise Exception("Method not implemented")
    
  
  # @abstractmethod
  # def select(self, user_input_id: int = None) -> List[DetectionResult]:
  #   """ abstractmethod """

  #   raise Exception("Method not implemented")