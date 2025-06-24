from bll.base.base_service import BaseService
from bll.schemas.user import UserIn, UserOut
from bll.schemas.profile import ProfileIn, ProfileOut
from dal.repositories import UserRepository
from dal.utils.enums import Entity


class UserService(BaseService[UserIn, UserOut, Entity.USER]):
    def __init__(self):
        super().__init__(UserRepository())

    def _to_out(self, model) -> UserOut:
        profile = None

        if model.profile:
            profile = ProfileOut(
                id=model.profile.id,
                bio=model.profile.bio
            )

        return UserOut(
            id=model.id,
            username=model.username,
            email=model.email,
            profile=profile
        )