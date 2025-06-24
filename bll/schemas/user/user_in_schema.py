from dataclasses import dataclass
from typing import Optional

from bll.schemas.profile import ProfileIn

@dataclass
class UserIn:
    username: str
    email: str
    profile: Optional[ProfileIn] = None