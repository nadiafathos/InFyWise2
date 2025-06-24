from marshmallow import EXCLUDE, Schema, fields, validate

class TagRequestSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
