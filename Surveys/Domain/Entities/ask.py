from dataclasses import dataclass, field
import uuid

@dataclass
class Ask:
    ask: str
    ask_uuid: str = field(default_factory=lambda: str(uuid.uuid4()))
    