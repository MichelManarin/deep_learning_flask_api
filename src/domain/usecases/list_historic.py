from typing import Dict
from abc import ABC, abstractclassmethod
from src.domain.models import Historic


class ListHistoric(ABC):
    """ Interface to ListHistoric use case """

    @abstractclassmethod
    def select(cls) -> Dict[bool, Historic]:
        """ Case """

        raise Exception("Should implement method: list")