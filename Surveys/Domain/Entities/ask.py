from dataclasses import dataclass, field
import uuid

@dataclass
class Ask:
    ask: str
    survey_uuid: str
    ask_uuid: str = field(default_factory=lambda: str(uuid.uuid4()))
    

    def to_dict(self):
        return {
            'ask': self.ask,
            'ask_uuid': self.ask_uuid,
            'survey_uuid': self.survey_uuid
        }
    

