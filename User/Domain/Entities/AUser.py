from dataclasses import dataclass

from User.Domain.Entities.UserType import UserType
from .Contact import Contact
from .Credentials import Credentials
import uuid

@dataclass
class AUser:
    user_uuid = str(uuid.uuid4())
    contact: Contact
    credentials: Credentials
    type: UserType