from marshmallow import Schema, fields

from api.schemas.tag import TagResponseSchema


class PostResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    content = fields.Str()
    author_id = fields.Int()
    tags = fields.List(fields.Nested(TagResponseSchema))