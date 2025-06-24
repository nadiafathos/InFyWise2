from dataclasses import dataclass
from typing import Optional

@dataclass
class ProfileOut:
    id: int
    bio: Optional[str]