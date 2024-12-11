import sqlalchemy as sa


class Config:
    def __init__(self, metadata):
        self.config = sa.Table(
            'config',
            metadata,
            sa.Column('tempo_verif', sa.Integer),
        )

    def insert(self, conn, tempo_verif):
        if not conn.execute(self.config.select()).fetchone():
            conn.execute(
                self.config.insert().values(tempo_verif=tempo_verif)
            )
        else:
            raise Exception("Only one configuration is allowed.")

    def select(self, conn):
        return conn.execute(self.config.select()).fetchone()._asdict()

    def update(self, conn, tempo_verif):
        conn.execute(self.config.update().values(tempo_verif=tempo_verif))

    def delete(self, conn):
        conn.execute(self.config.delete())
