from sqlalchemy import Column, String
from marshmallow import Schema, fields
from .entity import Entity, Base

class Log(Entity, Base):
    __tablename__ = 'logs'

    title = Column(String)
    description = Column(String)

    def __init__(self, title, description, created):
        Entity.__init__(self, created)
        self.title = title
        self.description = description

class LogSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()