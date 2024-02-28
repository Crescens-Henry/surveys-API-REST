from dataclasses import dataclass, field
import uuid

@dataclass
class AAward:
    name : str
    description : str
    award_uuid:  str = field(default_factory=lambda: str(uuid.uuid4()))
    