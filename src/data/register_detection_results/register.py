from typing import Type, Dict
from src.domain.usecases import RegisterDetectionResults as RegisterDetectionResultsInterface
from src.data.interfaces import DetectionResultsRepositoryInterface as DetectionResultsRepository
from src.domain.models import DetectionResult
from sqlalchemy.dialects.postgresql import JSONB


class RegisterDetectionResults(RegisterDetectionResultsInterface):
    """ Class to define usercase: Register Detection Results"""

    def __init__(self, detection_results_repository: Type[DetectionResultsRepository]):
        self.detection_results_repository = detection_results_repository

    def register(self, user_input_id: int, box: JSONB, number_fps: int, class_name: str, confidence: float) -> Dict[bool, DetectionResult]:
        """Register user use case
        :param - user_input_id: int
               - box: json 
               - number_fps: int
               - class_name: str
               - confidence: float
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_input_id, int) and isinstance(number_fps, int) and isinstance(class_name, str) and isinstance(confidence, float) 

        if validate_entry:
            response = self.detection_results_repository.insert(user_input_id=user_input_id, box=box, number_fps=number_fps, class_name=class_name, confidence=confidence)

        return {"Success": validate_entry, "Data": response}