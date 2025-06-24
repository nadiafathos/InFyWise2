from marshmallow import Schema, fields, EXCLUDE, validate

from api.schemas.profile import ProfileRequestSchema


class UserRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    username = fields.Str(required=True, validate=validate.Length(min=1, max=80))
    email = fields.Email(required=True)
    profile = fields.Nested(ProfileRequestSchema, required=False)
