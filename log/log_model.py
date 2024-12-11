import sqlalchemy as sa
from pydantic import BaseModel
from typing import Union


class LogModel:
    def __init__(self, metadata):
        self.log = sa.Table(
            'log',
            metadata,
            sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
            sa.Column('luz', sa.Integer),
            sa.Column('umidade', sa.Integer),
            sa.Column('created_at', sa.DateTime, default=sa.func.now())
        )

    def insert(self, conn, luz, umidade):
        conn.execute(self.log.insert().values(luz=luz, umidade=umidade))

    def select_all(self, conn):
        return conn.execute(self.log.select()).fetchall()

class BaseLog(BaseModel):
    id: Union[int, None] = None
    umidade: Union[int, None] = None
    luz: Union[int, None] = None
    created_at: Union[int, None] = None