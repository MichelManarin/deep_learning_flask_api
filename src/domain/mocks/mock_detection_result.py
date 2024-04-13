from faker import Faker
from src.domain.models import DetectionResult

faker = Faker()

def mock_detection_result() -> DetectionResult:
    """ Mocking DetectionResult """

    return DetectionResult(
        id=faker.random_number(digits=5), user_input_id=faker.random_number(digits=5), confidence=0.7,  number_fps=1, class_name=faker.name(), box=[]
    )