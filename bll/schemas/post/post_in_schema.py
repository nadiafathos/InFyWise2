from dataclasses import dataclass
from typing import Optional, List

from bll.schemas.tag import TagIn


@dataclass
class PostIn:
    title: str
    content: Optional[str]
    author_id: int
    tags: Optional[List[TagIn]] = None