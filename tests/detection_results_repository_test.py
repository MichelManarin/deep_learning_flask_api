import random
from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities import DetectionResult as DetectionResultModel
from src.infra.repo.detection_results_repository import DetectionResultRepository
from src.infra.entities import UserInput as UserInputModel
from src.infra.repo.user_input_repository import UserInputRepository
from datetime import datetime

faker = Faker()
detection_result_repository = DetectionResultRepository()
db_connection_handler = DBConnectionHandler()

def fake_random_float(start=0, end=100, precision=2):
    return round(random.uniform(start, end), precision)

def test_insert_detection_result():
  """ Should Insert Correctly """

  iou = fake_random_float()
  confidence = fake_random_float()
  video_path = "any_path"
  created_at = datetime.utcnow()
  user_input_id = 99998
  
  engine = db_connection_handler.get_engine()

  box = []
  class_name = faker.name()
  number_fps = 1

  engine.execute("INSERT INTO user_inputs (id, video_path, confidence, iou, created_at) VALUES ('{}','{}','{}','{}','{}')".format(
   user_input_id, video_path, confidence, iou, created_at ))
  
  new_detection_result_input = DetectionResultRepository.insert(user_input_id, box, class_name, confidence, number_fps)
 
  engine.execute("DELETE FROM detection_results WHERE user_input_id={}".format(user_input_id))
  engine.execute("DELETE FROM user_inputs WHERE id={}".format(user_input_id))

  assert new_detection_result_input.id == new_detection_result_input.id
  assert new_detection_result_input.confidence == new_detection_result_input.confidence
  assert new_detection_result_input.user_input_id == new_detection_result_input.user_input_id

   