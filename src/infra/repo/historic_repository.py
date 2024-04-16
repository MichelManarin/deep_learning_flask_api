from typing import List
from src.data.interfaces import HistoricRepositoryInterface
from src.infra.config import DBConnectionHandler
from src.domain.models import Historic

class HistoricRepository(HistoricRepositoryInterface):
  """
    Class to get Historic Repository
  """
  @classmethod
  def select(cls) -> List[Historic]:
    """ select historic data
    :return - list of tupple with Historic
    """
    with DBConnectionHandler() as db_connection:
      try:
        sql_query = """
          SELECT ui.id, dr.box, dr.number_fps, dr.class_name, dr.confidence, ui.iou, dr.created_at, ui.video_path, ui.id
            FROM (
                SELECT *
                FROM user_inputs
                ORDER BY created_at DESC
                LIMIT 10
            ) AS ui
          JOIN detection_results AS dr ON ui.id = dr.user_input_id
          ORDER BY ui.id desc, number_fps;
        """
        results = db_connection.session.execute(sql_query)

        result = []
        for row in results:
          result.append(Historic(
            id=row.id,
            video_path=row.video_path,
            confidence=row.confidence,
            iou=row.iou,
            created_at=row.created_at,
            box=row.box,
            number_fps=row.number_fps,
            class_name=row.class_name,
          ))
          
        return result
      except Exception as e:
          db_connection.session.rollback()
          raise e
      finally:
          db_connection.session.close()

    return []