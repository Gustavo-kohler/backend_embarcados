import sqlalchemy as sa
from pydantic import BaseModel
from typing import Union


class Config_base(BaseModel):
    tempo_verif: Union[int, None] = None
    umidade_max: Union[int, None] = None
    umidade_min: Union[int, None] = None


class Config:
    def __init__(self, metadata):
        self.config = sa.Table(
            'config',
            metadata,
            sa.Column('tempo_verif', sa.Integer),
            sa.Column('umidade_max', sa.Integer),
            sa.Column('umidade_min', sa.Integer),
        )

    def insert(self, conn, tempo_verif, umidade_max, umidade_min):
        if not conn.execute(self.config.select()).fetchone():
            conn.execute(
                self.config.insert().values(tempo_verif=tempo_verif, umidade_max=umidade_max, umidade_min=umidade_min)
            )
            conn.commit()
        else:
            raise Exception("Only one configuration is allowed.")

    def select(self, conn):
        result = conn.execute(self.config.select()).fetchone()
        if result is None:
            return None
        return result._asdict()

    def update(self, conn, tempo_verif, umidade_max, umidade_min):
        conn.execute(
            self.config.update().values(tempo_verif=tempo_verif, umidade_max=umidade_max, umidade_min=umidade_min))
        conn.commit()

    def delete(self, conn):
        conn.execute(self.config.delete())
        conn.commit()