from dataclasses import dataclass
import uuid

@dataclass
class ask:
    ask_uuid = str(uuid.uuid4())
    pregunta: str