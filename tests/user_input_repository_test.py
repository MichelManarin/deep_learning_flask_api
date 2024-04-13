import random
from faker import Faker
from src.infra.config import DBConnectionHandler
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