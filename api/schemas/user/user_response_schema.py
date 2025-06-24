from marshmallow import Schema, fields

from api.schemas.profile import ProfileResponseSchema


class UserResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    email = fields.Email()
    profile = fields.Nested(ProfileResponseSchema)
