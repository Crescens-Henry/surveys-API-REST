from dataclasses import dataclass, field
from Results.Domain.Entities.Result import Result
from Results.Domain.Entities.StatusResult import StatusResult
import uuid

@dataclass
class AResult:
    result_uuid  : str = field(default_factory=uuid.uuid4, init=False)
    result : Result
    statusResult : StatusResult
    