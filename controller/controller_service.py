import fastapi
from . import controller_model
import sqlalchemy as sa

app = fastapi.FastAPI()

engine = sa.create_engine('sqlite:///./database.db')
conn = engine.connect()
metadata = sa.MetaData()

planta = controller_model.Planta(metadata)
config = controller_model.Config(metadata)

metadata.create_all(engine)

config.insert(conn, None, None, False)


@app.get('/planta')
def get_planta():
    return planta.select_all(conn)

@app.get('/planta/{id}')
def get_planta_by_id(id):
    return planta.select_by_id(conn, id)

@app.post('/planta')
def post_planta(nome, umidade_max, umidade_min, luz_max, luz_min):
    planta.insert(conn, nome, umidade_max, umidade_min, luz_max, luz_min)
    return planta.select_all(conn)

@app.put('/planta/{id}')
def put_planta(id, nome, umidade_max, umidade_min, luz_max, luz_min):
    planta.update(conn, id, nome, umidade_max, umidade_min, luz_max, luz_min)
    return planta.select_by_id(conn, id)

@app.delete('/planta/{id}')
def delete_planta(id):
    planta.delete(conn, id)
    return planta.select_all(conn)

@app.get('/config')
def get_config():
    return config.select(conn)

@app.put('/config')
def put_config(planta_ativa, tempo_verif, modificado):
    config.update(conn, planta_ativa, tempo_verif, modificado)
    return config.select(conn)

