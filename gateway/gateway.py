import fastapi
import httpx
import uvicorn

app = fastapi.FastAPI(title='Gateway')

SERVICES = {
    'controller': 'http://0.0.0.0:8001',
    'log': 'http://0.0.0.0:8002'
}


@app.get("/{service}/{path:path}")
async def proxy_get(service: str, path: str):
    if service not in SERVICES:
        raise fastapi.HTTPException(status_code=404, detail="Service not found")
    url = f"{SERVICES[service]}/{path}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

@app.post("/{service}/{path:path}")
async def proxy_post(service: str, path: str, body: dict):
    if service not in SERVICES:
        raise fastapi.HTTPException(status_code=404, detail="Service not found")
    url = f"{SERVICES[service]}/{path}"
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=body)
    return response.json()

@app.put("/{service}/{path:path}")
async def proxy_put(service: str, path: str, body: dict):
    if service not in SERVICES:
        raise fastapi.HTTPException(status_code=404, detail="Service not found")
    url = f"{SERVICES[service]}/{path}"
    async with httpx.AsyncClient() as client:
        response = await client.put(url, json=body)
    return response.json()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)