
from marshmallow import Schema, fields
from sqlalchemy import Column, String

from .entity import Entity, Base

class Cmd(Entity, Base):
    __tablename__ = 'Cmds'

    name = Column(String)
    cmd = Column(String)

    def __init__(self, name, cmd, created):
        Entity.__init__(self, created)
        self.name = name
        self.cmd = cmd

class CmdSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    cmd = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()