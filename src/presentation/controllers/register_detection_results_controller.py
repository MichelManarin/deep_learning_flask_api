from typing import Type
from src.main.interface import RouteInterface
from src.domain.usecases import RegisterDetectionResults
from src.presentation.helpers import HttpRequest, HttpResponse
from src.presentation.errors import HttpErrors


class RegisterDetectionResultsController(RouteInterface):
    """ Class to Define Route to register_detection_results use case """

    def __init__(self, register_detection_results: Type[RegisterDetectionResults]):
        self.register_detection_results = register_detection_results

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """

        response = None

        if http_request.body:
            # if body in htp_request

            body_params = http_request.body.keys()

            if "user_input_id" in body_params and "number_fps" in body_params and "image_base64" in body_params:
                user_input_id = http_request.body["user_input_id"]
                number_fps = http_request.body["number_fps"]
                image_base64 = http_request.body["image_base64"]
                
                response = self.register_detection_results.register(
                    user_input_id=user_input_id, number_fps=number_fps, image_base64=image_base64 
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