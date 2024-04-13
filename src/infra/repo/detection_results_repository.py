from src.infra.config import DBConnectionHandler
from src.infra.entities import DetectionResult


class DetectionResultRepository:
    """
    Class to manage Detection Result Repository
    """

    @classmethod
    def insert(cls, user_input_id: int, box: dict, class_name: str, confidence: float) -> DetectionResult:
        """ Insert data into detection result entity
        :param - user_input_id: int
               - box: dict
               - class_name: str
               - confidence: float
        :return - tuple with new detection result
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_result = DetectionResult(user_input_id=user_input_id, box=box, class_name=class_name, confidence=confidence)
                db_connection.session.add(new_result)
                db_connection.session.commit()
                return new_result
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def get_by_id(cls, detection_result_id: int) -> DetectionResult:
        """ Get detection result by ID
        :param - detection_result_id: int
        :return - DetectionResult object or None if not found
        """

        with DBConnectionHandler() as db_connection:
            result = db_connection.session.query(DetectionResult).filter_by(id=detection_result_id).first()
            return result
