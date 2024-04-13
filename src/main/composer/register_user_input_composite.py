from src.main.interface import RouteInterface
from src.presentation.controllers import RegisterUserInputController
from src.data.register_input_user.register import RegisterUserInput
from src.infra.repo.user_input_repository import UserInputRepository


def register_user_input_composer() -> RouteInterface:
    """Composing Register User Route
    :param - None
    :return - Object with Register User Route
    """

    repository = UserInputRepository()
    use_case = RegisterUserInput(repository)
    register_user_route = RegisterUserInputController(use_case)

    return register_user_route