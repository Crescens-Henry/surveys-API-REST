from dataclasses import dataclass, field

from User.Domain.Entities.UserType import UserType
from .Contact import Contact
from .Credentials import Credentials
import uuid

@dataclass
class AUser:
    user_uuid :str = field(default_factory=lambda: str(uuid.uuid4()))
    contact: Contact
    credentials: Credentials
    type: UserType