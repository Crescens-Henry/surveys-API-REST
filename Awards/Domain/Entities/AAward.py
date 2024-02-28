from dataclasses import dataclass
import uuid

@dataclass
class AAward:
    award_uuid  = str(uuid.uuid4())
    name : str
    description : str