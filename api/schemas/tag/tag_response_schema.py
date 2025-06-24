from marshmallow import Schema, fields

class TagResponseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
