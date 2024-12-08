import sqlalchemy as sa


class Planta:
    def __init__(self, metadata):
        self.planta = sa.Table(
            'planta',
            metadata,
            sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
            sa.Column('nome', sa.String(255)),
            sa.Column('umidade_max', sa.Integer),
            sa.Column('umidade_min', sa.Integer),
            sa.Column('luz_max', sa.Integer),
            sa.Column('luz_min', sa.Integer),
        )

    def insert(self, conn, nome, umidade_max, umidade_min, luz_max, luz_min):
        conn.execute(
            self.planta.insert().values(nome=nome, umidade_max=umidade_max, umidade_min=umidade_min, luz_max=luz_max,
                                        luz_min=luz_min))

    def select_all(self, conn):
        return [row._asdict() for row in conn.execute(self.planta.select()).fetchall()]

    def select_by_id(self, conn, id):
        return conn.execute(self.planta.select().where(self.planta.c.id == id)).fetchone()._asdict()

    def update(self, conn, id, nome, umidade_max, umidade_min, luz_max, luz_min):
        conn.execute(self.planta.update().where(self.planta.c.id == id).values(nome=nome, umidade_max=umidade_max,
                                                                               umidade_min=umidade_min, luz_max=luz_max,
                                                                               luz_min=luz_min))

    def delete(self, conn, id):
        conn.execute(self.planta.delete().where(self.planta.c.id == id))

