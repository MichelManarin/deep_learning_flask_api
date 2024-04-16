from typing import Type
from src.main.interface import RouteInterface
from src.domain.usecases import ListHistoric
from src.presentation.helpers import HttpRequest, HttpResponse
from src.presentation.errors import HttpErrors

class ListHistoricController(RouteInterface):
    """ Class to Define Route to list_historic use case """

    def __init__(self, list_historic_use_case: Type[ListHistoric]):
        self.list_historic_use_case = list_historic_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """
        try:
          response = self.list_historic_use_case.select()

          return HttpResponse(status_code=200, body=response["Data"])
        except:
          https_error = HttpErrors.error_400()
          return HttpResponse(
            status_code=https_error["status_code"]
          )