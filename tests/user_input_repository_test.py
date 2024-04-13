import random
from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities import UserInput as UserInputModel
from src.infra.repo.user_input_repository import UserInputRepository

faker = Faker()
user_input_repository = UserInputRepository()
db_connection_handler = DBConnectionHandler()

def fake_random_float(start=0, end=100, precision=2):
    return round(random.uniform(start, end), precision)

def test_insert_user_input():
  """ Should Insert Correctly """

  path = faker.word()
  confidence = fake_random_float()
  iou = fake_random_float()
  engine = db_connection_handler.get_engine()

  new_user_input = user_input_repository.insert(path, confidence, iou)
  query_user_input = engine.execute(
        "SELECT * FROM user_inputs WHERE id='{}';".format(new_user_input.id)
    ).fetchone()
  
  engine.execute("DELETE FROM user_inputs WHERE id='{}'".format(new_user_input.id))
  
  assert new_user_input.id == query_user_input.id
  assert new_user_input.confidence == query_user_input.confidence
  assert new_user_input.iou == query_user_input.iou

def test_select_user_input():
   """ Should select a user in UserInputs table and compare it """

   user_input_id = 99999
   path = faker.word()
   confidence = fake_random_float()
   iou = fake_random_float()
   data = UserInputModel(id=user_input_id, confidence=confidence, iou=iou, video_path=path)

   engine = db_connection_handler.get_engine()
   engine.execute(
      "INSERT INTO user_inputs (id, confidence, iou, video_path) VALUES ('{}', '{}', '{}', '{}');".format(
         user_input_id, confidence, iou, path
      )
   )

   query_user_input = user_input_repository.select(user_input_id=user_input_id)

   assert data in query_user_input

   engine.execute("DELETE FROM user_inputs WHERE id='{}';".format(user_input_id))