from dataclasses import dataclass, field
import uuid

@dataclass
class ASurvey:
    title: str 
    survey_uuid: str = field(default_factory=lambda: str(uuid.uuid4()))
    
   