import fastapi
from .models import planta_model, config_model, base_model
import sqlalchemy as sa
import requests

URLEmbarcado = ""

app = fastapi.FastAPI()

engine = sa.create_engine('sqlite:///./database.db')
conn = engine.connect()
metadata = sa.MetaData()

planta = planta_model.Planta(metadata)
config = config_model.Config(metadata)

metadata.create_all(engine)

config.insert(conn, None)


@app.get('/planta')
def get_planta():
    return planta.select_all(conn)

@app.get('/planta/{id}')
def get_planta_by_id(id: int):
    return planta.select_by_id(conn, id)

@app.post('/planta')
def post_planta(planta_data: base_model.Planta_base):
    planta.insert(conn, planta_data.nome, planta_data.umidade_max, planta_data.umidade_min, planta_data.luz_max, planta_data.luz_min)
    return planta.select_all(conn)

@app.put('/planta/{id}')
def put_planta(id: int, planta_data: base_model.Planta_base):
    planta.update(conn, id, planta_data.nome, planta_data.umidade_max, planta_data.umidade_min, planta_data.luz_max, planta_data.luz_min)
    return planta.select_by_id(conn, id)

@app.delete('/planta/{id}')
def delete_planta(id: int):
    planta.delete(conn, id)
    return planta.select_all(conn)

@app.get('/config')
def get_config():
    return config.select(conn)

@app.put('/config')
def put_config(config_data: base_model.Config_base):
    config.update(conn, config_data.tempo_verif)
    requests.post(URLEmbarcado, json = config_data)
    return config.select(conn)
