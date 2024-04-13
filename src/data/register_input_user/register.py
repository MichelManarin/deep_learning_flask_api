from typing import Type, Dict
from src.domain.usecases import RegisterUserInput as RegisterUserInputInterface
from src.data.interfaces import UserInputRepositoryInterface as UserInputRepository
from src.domain.models import UserInput


class RegisterUserInput(RegisterUserInputInterface):
    """ Class to define usercase: Register User Input"""

    def __init__(self, user_input_repository: Type[UserInputRepository]):
        self.user_input_repository = user_input_repository

    def register(self, path: str, confidence: float, iou: float) -> Dict[bool, UserInput]:
        """Register user use case
        :param - path: path file
               - confidence: confidence
               - iou
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(path, str) and isinstance(confidence, float) and isinstance(iou, float)

        if validate_entry:
            response = self.user_input_repository.insert(path, confidence, iou)

        return {"Success": validate_entry, "Data": response}