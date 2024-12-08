import sqlalchemy as sa


class Config:
    def __init__(self, metadata):
        self.config = sa.Table(
            'config',
            metadata,
            sa.Column('planta_ativa', sa.Integer, sa.ForeignKey('planta.id')),
            sa.Column('tempo_verif', sa.Integer),
            sa.Column('modificado', sa.Boolean),
        )

    def insert(self, conn, planta_ativa, tempo_verif, modificado):
        if not conn.execute(self.config.select()).fetchone():
            conn.execute(
                self.config.insert().values(planta_ativa=planta_ativa, tempo_verif=tempo_verif, modificado=modificado)
            )
        else:
            raise Exception("Only one configuration is allowed.")

    def select(self, conn):
        return conn.execute(self.config.select()).fetchone()._asdict()

    def update(self, conn, planta_ativa, tempo_verif, modificado):
        conn.execute(self.config.update().values(planta_ativa=planta_ativa, tempo_verif=tempo_verif, modificado=modificado))

    def delete(self, conn):
        conn.execute(self.config.delete())

    def update_modificado(self, conn, modificado):
        conn.execute(self.config.update().values(modificado=modificado))

    def select_modificado(self, conn):
        return conn.execute(self.config.select().where(self.config.c.modificado == True)).fetchone()
