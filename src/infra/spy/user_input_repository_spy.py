from typing import List
from src.domain.models import UserInput
from src.domain.mocks import mock_user_input


class UserInputRepositorySpy:
    """ Spy to User Repository """

    def __init__(self):
        self.insert_user_input_params = {}
        self.select_user_input_params = {}

    def insert(self, path: str, iou: float, confidence: float) -> UserInput:
        """ Spy to all the attributes """

        self.insert_user_input_params["path"] = path
        self.insert_user_input_params["iou"] = iou
        self.insert_user_input_params["confidence"] = confidence

        return mock_user_input()

    def select(self, user_input_id: int = None, path: str = None, iou: float = None, confidence: float = None) -> List[UserInput]:
        """ Spy to all the attributes """

        self.select_user_input_params["user_input_id"] = user_input_id
        self.select_user_input_params["confidence"] = confidence
        self.select_user_input_params["path"] = path
        self.select_user_input_params["iou"] = iou

        return [mock_user_input()]