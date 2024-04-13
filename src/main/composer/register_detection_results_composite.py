from src.main.interface import RouteInterface
from src.presentation.controllers import RegisterDetectionResultsController
from src.data.register_detection_results.register import RegisterDetectionResults
from src.infra.repo.detection_results_repository import DetectionResultRepository


def register_detection_results_composer() -> RouteInterface:
    """Composing Register Detection Results
    :param - None
    :return - Object with Register User Route
    """

    repository = DetectionResultRepository()
    use_case = RegisterDetectionResults(repository)
    register_user_route = RegisterDetectionResultsController(use_case)

    return register_user_route