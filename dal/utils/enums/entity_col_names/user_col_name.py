from enum import Enum

class UserCol(Enum):
    ID = "user_id"
    USERNAME = "username"
    EMAIL = "email"
    PROFILE = 'profile'
    POSTS = 'posts'

class ProfileCol(Enum):
    ID = "profile_id"
    BIO = "bio"
    FK_USER = "user_id"
    USER = 'user'
