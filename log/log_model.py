import sqlalchemy as sa


class LogModel:
    def __init__(self, metadata):
        self.log = sa.Table(
            'log',
            metadata,
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('message', sa.String(255)),
            sa.Column('created_at', sa.DateTime, default=sa.func.now())
        )

    def insert(self, conn, message):
        conn.execute(self.log.insert().values(message=message))

    def select_all(self, conn):
        return conn.execute(self.log.select()).fetchall()

