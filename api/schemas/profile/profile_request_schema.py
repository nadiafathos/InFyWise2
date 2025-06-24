from marshmallow import EXCLUDE, Schema, fields, validate


class ProfileRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    bio = fields.Str(required=False, allow_none=True, validate=validate.Length(max=200))
