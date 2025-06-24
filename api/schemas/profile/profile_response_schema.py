from marshmallow import Schema, fields

class ProfileResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    bio = fields.Str()