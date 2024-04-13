from faker import Faker
from src.data.register_input_user.register import RegisterUserInput
from src.infra.spy.user_input_repository_spy import UserInputRepositorySpy

faker = Faker()

def test_register():
    """ Testing registry method """

    user_input_repo = UserInputRepositorySpy()
    register_input_user = RegisterUserInput(user_input_repo)

    attributes = {"path": faker.name(), "iou": 0.7, "confidence": 0.7}

    response = register_input_user.register(
        path=attributes["path"], iou=attributes["iou"], confidence=attributes["confidence"]
    )

    # Testing inputs
    assert user_input_repo.insert_user_input_params["path"] == attributes["path"]
    assert user_input_repo.insert_user_input_params["iou"] == attributes["iou"]
    assert user_input_repo.insert_user_input_params["confidence"] == attributes["confidence"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]