import fastapi
from config_model import Config, Config_base
import sqlalchemy as sa
import uvicorn

URLEmbarcado = ""

app = fastapi.FastAPI(title='Controller')

engine = sa.create_engine('sqlite:///./controller/controller.db')
conn = engine.connect()
metadata = sa.MetaData()

config = Config(metadata)

metadata.create_all(engine)


@app.get('/')
def get_config():
    if not config.select(conn):
        config.insert(conn, None, None, None)
    return config.select(conn)


@app.put('/')
def put_config(config_data: Config_base):
    config.update(conn, config_data.tempo_verif, config_data.umidade_max, config_data.umidade_min)
    #requests.post(URLEmbarcado, json=config_data)
    return config.select(conn)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)