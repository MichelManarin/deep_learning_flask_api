# from faker import Faker
# from src.data.register_detection_results import RegisterDetectionResults
# from src.infra.spy.detection_results_repository_spy import DetectionResultsRepositorySpy
# from src.infra.spy.user_input_repository_spy import UserInputRepositorySpy

# faker = Faker()

# def test_register():
#     """ Testing registry method """

#     user_input_repository = UserInputRepositorySpy()
#     detection_results_repository = DetectionResultsRepositorySpy()
#     register_detection_results = RegisterDetectionResults(detection_results_repository, user_input_repository)

#     attributes = {"number_fps": 1, "image_base64": "", "user_input_id": 9998 }

#     response = register_detection_results.register(
#         number_fps=attributes["number_fps"], user_input_id=attributes["user_input_id"], class_name=attributes["image_base64"]
#     )

#     # Testing inputs
#     assert detection_results_repository.insert_detection_results_params["user_input_id"] == attributes["user_input_id"]

#     # Testing outputs
#     assert response["Success"] is True
#     assert response["Data"]