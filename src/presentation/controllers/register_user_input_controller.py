from typing import Type
from src.main.interface import RouteInterface
from src.domain.usecases import RegisterUserInput
from src.presentation.helpers import HttpRequest, HttpResponse
from src.presentation.errors import HttpErrors


class RegisterUserInputController(RouteInterface):
    """ Class to Define Route to register_user_input use case """

    def __init__(self, register_user_input_use_case: Type[RegisterUserInput]):
        self.register_user_input_use_case = register_user_input_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """

        response = None

        if http_request.body:
            # if body in htp_request

            body_params = http_request.body.keys()

            if "path" in body_params and "iou" in body_params and "confidence" in body_params:
                path = http_request.body["path"]
                iou = http_request.body["iou"]
                confidence = http_request.body["confidence"]
                response = self.register_user_input_use_case.register(
                    path=path, iou=iou, confidence=confidence, 
                )

            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"]
                )

            return HttpResponse(status_code=200, body=response["Data"])

        # If no body in http_request
        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"]
        )