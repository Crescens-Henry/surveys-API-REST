from dataclasses import dataclass, field
import uuid


@dataclass
class ASurvey:
    survey_uuid: str = field(default_factory=lambda: str(uuid.uuid4()))
    titulo: str = ""