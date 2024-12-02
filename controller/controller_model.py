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
        return conn.execute(self.planta.select()).fetchall()

    def select_by_id(self, conn, id):
        return conn.execute(self.planta.select().where(self.planta.c.id == id)).fetchone()

    def update(self, conn, id, nome, umidade_max, umidade_min, luz_max, luz_min):
        conn.execute(self.planta.update().where(self.planta.c.id == id).values(nome=nome, umidade_max=umidade_max,
                                                                               umidade_min=umidade_min, luz_max=luz_max,
                                                                               luz_min=luz_min))

    def delete(self, conn, id):
        conn.execute(self.planta.delete().where(self.planta.c.id == id))


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
        return conn.execute(self.config.select()).fetchone()

    def update(self, conn, planta_ativa, tempo_verif, modificado):
        conn.execute(self.config.update().values(planta_ativa=planta_ativa, tempo_verif=tempo_verif, modificado=modificado))

    def delete(self, conn):
        conn.execute(self.config.delete())

    def update_modificado(self, conn, modificado):
        conn.execute(self.config.update().values(modificado=modificado))

    def select_modificado(self, conn):
        return conn.execute(self.config.select().where(self.config.c.modificado == True)).fetchone()
