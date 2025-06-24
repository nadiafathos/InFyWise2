from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from bll.schemas.tag import TagOut


@dataclass
class PostOut:
    id: int
    title: str
    content: Optional[str]
    author_id: int
    tags: List[TagOut]