from enum import Enum

class Table(Enum):
    POST = "posts"
    TAG = "tags"
    USER = "users"
    PROFILE = "profiles"
    POST_TAG = "post_tags"
    PATIENT = "patients"
    ROLE = "roles"
    DOCTOR = "doctor"
    SYMPTOM= "symptom"

class Entity(Enum):
    POST = "Post"
    TAG = "Tag"
    USER = "User"
    PROFILE = "Profile"
    POST_TAG = "Post_tag"
    APPOINTMENT = "appointment"
    SYMPTOM = "symptom"
    TESTIMONY = "testimony"
    DISEASE = "disease"
    ROLE = "role"
    DOCTOR = "doctor"


