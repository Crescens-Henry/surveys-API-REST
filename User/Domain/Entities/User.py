from dataclasses import dataclass
from .Contact import Contact
from .Credentials import Credentials
import uuid

@dataclass
class User:
    user_uuid = str(uuid.uuid4())
    contact: Contact
    credentials: Credentials
