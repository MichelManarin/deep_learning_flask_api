import base64
from io import BytesIO
from PIL import Image

from typing import Type, Dict
from src.domain.usecases import RegisterDetectionResults as RegisterDetectionResultsInterface
from src.data.interfaces import DetectionResultsRepositoryInterface as DetectionResultsRepository
from src.data.interfaces import UserInputRepositoryInterface as UserInputRepository
from src.domain.models import DetectionResult
from sqlalchemy.dialects.postgresql import JSONB
from src.infra.neural_network import Model

model = Model("yolov8s")

class RegisterDetectionResults(RegisterDetectionResultsInterface):
    """ Class to define usercase: Register Detection Results"""

    def __init__(self, detection_results_repository: Type[DetectionResultsRepository], user_input_repository: Type[UserInputRepository]):
        self.detection_results_repository = detection_results_repository
        self.user_input_repository = user_input_repository

    def register(self, user_input_id: int, number_fps: int, image_base64: str) -> Dict[bool, DetectionResult]:
        """Register user use case
        :param - user_input_id: int
               - box: json 
               - number_fps: int
               - class_name: str
               - confidence: float
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(user_input_id, int) and isinstance(number_fps, int) and isinstance(image_base64, str) 

        if validate_entry:
            user_input = self.user_input_repository.select(user_input_id)

            iou = user_input.iou
            confidence = user_input.confidence
            
            image_bytes = base64.b64decode(image_base64)
            image_buffer = BytesIO(image_bytes)
            image = Image.open(image_buffer)
            image_rgb = image.convert('RGB')
                      
            predictions = model(image_rgb, confidence, iou)
            detections = [p.to_dict() for p in predictions]

            insert_results = []
            for detection in detections:
                insert_result = self.detection_results_repository.insert(user_input_id=user_input_id, box=detection['box'], number_fps=number_fps, class_name= detection['class_name'], confidence=detection['confidence'])
                insert_results.append(insert_result)

            response = { "detections": insert_results }

        return {"Success": validate_entry, "Data": response}