from typing import Type, Dict
from src.domain.usecases import ListHistoric as ListHistoricInterface
from src.data.interfaces import HistoricRepositoryInterface as HistoricRepository
from src.domain.models import Historic


class ListHistoric(ListHistoricInterface):
    """ Class to define usercase: List Historic """

    def __init__(self, historic_repository: Type[HistoricRepository]):
        self.historic_repository = historic_repository

    def select(self) -> Dict[bool, Historic]:
        """Lister user use case
        :param - user_input_id: int
        :return - Dictionary with informations of the historic
        """

        response = self.historic_repository.select()

        return {"Success": True, "Data": response}