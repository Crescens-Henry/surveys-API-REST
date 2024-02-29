from dataclasses import dataclass, field
from CorrectResults.Domain.Entities.Type_status import Type_status
import uuid

@dataclass
class ACorrectResults:
    correctResults_uuid  : str = field(default_factory=uuid.uuid4, init=False)
    valueRes : Type_status
    