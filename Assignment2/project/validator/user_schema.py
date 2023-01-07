from marshmallow import Schema, fields, validate


class getPDFSchema(Schema):
    fullName = fields.Str(required=True, validate=validate.Length(min=8))
    email = fields.Email(required=True)
    phone = fields.Int(required=True, validate=validate.Range(min=10))

#//test