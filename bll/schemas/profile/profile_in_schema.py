from dataclasses import dataclass
from typing import Optional

@dataclass
class ProfileIn:
    bio: Optional[str] = None