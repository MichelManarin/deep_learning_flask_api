from faker import Faker
from src.data.register_detection_results import RegisterDetectionResults
from src.infra.spy.detection_results_repository_spy import DetectionResultsRepositorySpy

faker = Faker()

def test_register():
    """ Testing registry method """

    detection_results_repository = DetectionResultsRepositorySpy()
    register_detection_results = RegisterDetectionResults(detection_results_repository)

    attributes = {"number_fps": 1, "confidence": 0.7, "user_input_id": 9998, "box": [], "class_name": faker.name(), "confidence": 0.5}

    response = register_detection_results.register(
        number_fps=attributes["number_fps"], confidence=attributes["confidence"], user_input_id=attributes["user_input_id"], box=attributes["box"], class_name=attributes["class_name"]
    )

    # Testing inputs
    assert detection_results_repository.insert_detection_results_params["confidence"] == attributes["confidence"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]