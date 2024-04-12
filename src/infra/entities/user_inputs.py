from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.infra.config import Base
from datetime import datetime

class UserInput(Base):
    """ UserInput Entity """

    __tablename__ = "user_inputs"

    id = Column(Integer, primary_key=True)
    video_path = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    iou = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    detection_results = relationship("DetectionResult", back_populates="user_input")

    def __repr__(self):
        return f"UserInput [id={self.id}, video_path={self.video_path}]"