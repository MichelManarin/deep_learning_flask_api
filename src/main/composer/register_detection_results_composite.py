from src.main.interface import RouteInterface
from src.presentation.controllers import RegisterDetectionResultsController
from src.data.register_detection_results.register import RegisterDetectionResults
from src.infra.repo.detection_results_repository import DetectionResultRepository
from src.infra.repo.user_input_repository import UserInputRepository


def register_detection_results_composer() -> RouteInterface:
    """Composing Register Detection Results
    :param - None
    :return - Object with Register User Route
    """
    user_input_repository = UserInputRepository()
    detection_repository = DetectionResultRepository()
    use_case_detection_results = RegisterDetectionResults(detection_repository, user_input_repository)
    register_user_route = RegisterDetectionResultsController(use_case_detection_results)

    return register_user_route