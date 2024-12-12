import fastapi
import requests
import uvicorn

from log_model import Log, Log_base
import sqlalchemy as sa

URLEmbarcado = ""

app = fastapi.FastAPI(title='Log')

engine = sa.create_engine('sqlite:///./log/log.db')
conn = engine.connect()
metadata = sa.MetaData()

log = Log(metadata)

metadata.create_all(engine)


@app.post('/')
def post_log(log_data: Log_base):
    log.insert(conn, log_data.luz, log_data.umidade)
    return log.select_all(conn)

@app.get('/')
def get_log():
    return log.select_all(conn)

@app.get('/spike')
def get_spike():
    #request.get(URLEmbarcado)
    return log.select_all(conn)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8002)