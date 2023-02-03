from fastapi import FastAPI, WebSocket
from wshandler import WsHandler

app = FastAPI()
handler = WsHandler()


@app.get("/")
def root():
    return "Heklo :)"

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await handler.connect(websocket)

    while True:
        data = await websocket.receive_json()