from bll.base.base_service import BaseService
from bll.schemas.post import PostIn, PostOut
from bll.schemas.tag import TagOut
from dal.repositories import PostRepository, TagRepository
from dal.utils.enums import Entity, TagCol


class PostService(BaseService[PostIn, PostOut, Entity.POST]):
    def __init__(self):
        super().__init__(PostRepository())

    def create(self, data: PostIn) -> PostOut:
        post = self.repo.create(
            title=data.title,
            content=data.content,
            author_id=data.author_id
        )
        if data.tags:
            for t in data.tags:
                tag = (TagRepository()
                       .get_by(
                            column_name=TagCol.NAME.value,
                            value=t.name )
                       or TagRepository().create(**t.__dict__))

                self.repo.add_tag(post, tag)
        return self._to_out(post)

    def _to_out(self, model) -> PostOut:
        tags = [TagOut(id=tag.id, name=tag.name) for tag in model.tags]
        return PostOut(
            id=model.id,
            title=model.title,
            content=model.content,
            author_id=model.author_id,
            tags=tags,
        )