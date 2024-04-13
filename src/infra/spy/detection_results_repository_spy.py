from typing import List
from src.domain.models import DetectionResult
from src.domain.mocks import mock_detection_result
from sqlalchemy.dialects.postgresql import JSONB


class DetectionResultsRepositorySpy:
    """ Spy to Detection Results Repository """

    def __init__(self):
        self.insert_detection_results_params = {}
        self.select_detection_resultst_params = {}

    def insert(self, user_input_id: int, box: JSONB, number_fps: int, class_name: str, confidence: float) -> DetectionResult:
        """ Spy to all the attributes """

        self.insert_detection_results_params["user_input_id"] = user_input_id
        self.insert_detection_results_params["box"] = box
        self.insert_detection_results_params["number_fps"] = number_fps
        self.insert_detection_results_params["class_name"] = class_name
        self.insert_detection_results_params["confidence"] = confidence

        return mock_detection_result()