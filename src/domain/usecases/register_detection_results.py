from typing import Dict
from abc import ABC, abstractclassmethod
from src.domain.models import DetectionResult
from sqlalchemy.dialects.postgresql import JSONB


class RegisterDetectionResults(ABC):
    """ Interface to RegisterDetectionResults use case """

    @abstractclassmethod
    def register(cls, user_input_id: int, number_fps: int, image_base64: str) -> Dict[bool, DetectionResult]:
        """ Case """

        raise Exception("Should implement method: register")