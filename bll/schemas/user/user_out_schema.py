from dataclasses import dataclass
from typing import Optional
from datetime import datetime

from bll.schemas.profile import ProfileOut

@dataclass
class UserOut:
    id: int
    username: str
    email: str
    profile: Optional[ProfileOut]