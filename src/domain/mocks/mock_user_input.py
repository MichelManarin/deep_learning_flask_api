from faker import Faker
from src.domain.models import UserInput

faker = Faker()

def mock_user_input() -> UserInput:
    """ Mocking UserInput """

    return UserInput(
        id=faker.random_number(digits=5), path=faker.name(), confidence=0.7,  iou=0.5
    )