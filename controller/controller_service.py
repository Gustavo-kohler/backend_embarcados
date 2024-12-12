import fastapi
from config_model import Config, Config_base
import sqlalchemy as sa

URLEmbarcado = ""

app = fastapi.FastAPI()

engine = sa.create_engine('sqlite:///./controller/controller.db')
conn = engine.connect()
metadata = sa.MetaData()

config = Config(metadata)

metadata.create_all(engine)


@app.get('/config')
def get_config():
    if not config.select(conn):
        config.insert(conn, None, None, None)
    return config.select(conn)


@app.put('/config')
def put_config(config_data: Config_base):
    config.update(conn, config_data.tempo_verif, config_data.umidade_max, config_data.umidade_min)
    #requests.post(URLEmbarcado, json=config_data)
    return config.select(conn)
