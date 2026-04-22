import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://localhost:8000/ws/test_user"
    async with websockets.connect(uri) as websocket:
        print(f"Connected to {uri}")

        # Send generate_story message
        generate_message = {
            "type": "generate_story",
            "data": "a cute rabbit jumping over a rainbow"
        }
        await websocket.send(json.dumps(generate_message))
        print(f"Sent: {generate_message}")

        try:
            while True:
                message = await websocket.recv()
                print(f"Received: {message}")
        except websockets.exceptions.ConnectionClosedOK:
            print("Connection closed by server.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_websocket())
