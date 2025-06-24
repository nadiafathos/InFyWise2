from enum import Enum

class Table(Enum):
    POST = "posts"
    TAG = "tags"
    USER = "users"
    PROFILE = "profiles"
    POST_TAG = "post_tags"

class Entity(Enum):
    POST = "Post"
    TAG = "Tag"
    USER = "User"
    PROFILE = "Profile"
    POST_TAG = "Post_tag"
