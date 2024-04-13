from typing import Dict
from abc import ABC, abstractclassmethod
from src.domain.models import UserInput


class RegisterUserInput(ABC):
    """ Interface to RegisterUserInput use case """

    @abstractclassmethod
    def register(cls, name: str, password: str) -> Dict[bool, UserInput]:
        """ Case """

        raise Exception("Should implement method: register")