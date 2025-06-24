from enum import Enum


class PostTagCol(Enum):
    FK_POST = "post_id"
    FK_TAG = "tag_id"


class PostCol(Enum):
    ID = "post_id"
    TITLE = "title"
    CONTENT = "content"
    FK_AUTHOR = "author_id"
    AUTHOR = 'author'
    TAGS = 'tags'