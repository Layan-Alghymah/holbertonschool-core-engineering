#!/usr/bin/env python3
"""WebSocket broadcast server."""

import asyncio
import websockets


connected_clients = set()


async def connection_handler(websocket):
    """Handle messages and broadcast to all clients."""
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            for client in connected_clients.copy():
                await client.send("B:" + message)
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the WebSocket broadcast server."""
    async with websockets.serve(
        connection_handler, "127.0.0.1", 8765
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
