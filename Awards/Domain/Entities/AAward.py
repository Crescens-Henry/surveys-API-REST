from dataclasses import dataclass, field
import uuid

@dataclass
class AAward:
    award_uuid :str = field(default_factory=lambda: str(uuid.uuid4()))
    name : str
    description : str