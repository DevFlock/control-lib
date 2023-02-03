from fastapi import WebSocket
from enum import Enum

class Right:
    none = 99
    root = 0
    admin = 1


class WsHandler:
    def __init__(self) -> None:
        self.clients: list[WebSocket] = []
    
    async def connect(self, ws: WebSocket) -> WebSocket:
        await ws.accept()

        self.clients.append(ws)
        return ws
    
    def promote(self, client: WebSocket, right: Right):
        client.right = right