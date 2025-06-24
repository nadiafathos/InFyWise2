from marshmallow import EXCLUDE, Schema, fields, validate

from api.schemas.tag import TagRequestSchema


class PostRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    title = fields.Str(required=True, validate=validate.Length(min=1, max=120))
    content = fields.Str(required=False, allow_none=True)
    author_id = fields.Int(required=True)
    tags = fields.List(fields.Nested(TagRequestSchema), required=False)
