from src.main.interface import RouteInterface
from src.presentation.controllers import ListHistoricController
from src.data.historic.list import ListHistoric
from src.infra.repo.historic_repository import HistoricRepository


def list_historic_composer() -> RouteInterface:
    """Composing List Historic 
    :param - None
    :return - Object with Historic
    """

    repository = HistoricRepository()
    use_case = ListHistoric(repository)
    list_historic_route = ListHistoricController(use_case)

    return list_historic_route