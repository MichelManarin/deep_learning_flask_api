from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from src.infra.config import Base
from datetime import datetime

class DetectionResult(Base):
    """ DetectionResult Entity """

    __tablename__ = "detection_results"

    id = Column(Integer, primary_key=True)
    user_input_id = Column(Integer, ForeignKey("user_inputs.id"))
    box = Column(JSONB, nullable=False)
    class_name = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_input = relationship("UserInput", back_populates="detection_results")

    def __repr__(self):
        return f"DetectionResult [id={self.id}, class_name={self.class_name}]"
    
    def __eq__(self, other):
        if (self.id == other.id 
            and self.box == other.box 
            and self.class_name == other.class_name 
            and self.confidence == other.confidence 
            and self.user_input_id == other.user_input_id):
            return True
        return False