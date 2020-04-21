import json
import threading
import time
import websocket
import config
import utils
from . import channel_points

logger = utils.get_logger()

def pubsub():
    ws = websocket.WebSocketApp("wss://pubsub-edge.twitch.tv",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

def on_open(ws):
    logger.info("WebSocket connection open")
    listen_channel_points(ws)
    threading.Thread(target=ping_worker, args=[ws]).start()

def on_message(ws, message_str):
    logger.info("Received WebSocket message")
    message = json.loads(message_str)
    logger.debug(message)

    if message["type"] == "RESPONSE":
        if message["error"]:
            logger.error("Failed to listen to the {} topic".format("channel_points")) # TODO
        else:
            logger.info("Successfully listening to the {} topic".format("channel_points")) # TODO
    elif message["type"] == "MESSAGE":
        channel_points_message = json.loads(message["data"]["message"])
        channel_points.handle_message(channel_points_message)
    elif message["type"] == "PONG":
        pass # Normal response to a PING message. Do nothing.
    elif message["type"] == "RECONNECT": 
        pass # TODO

def on_error(ws, error):
    logger.error("WebSocket error:")
    logger.error(error)

def on_close(ws):
    logger.info("WebSocket connection closed")

def listen_channel_points(ws):
    logger.info("Attempting to listen to the channel points topic")
    topics = ["channel-points-channel-v1.{}".format(config.channel_id)]
    listen = {
        "type": "LISTEN",
        "data": {
            "topics": topics,
            "auth_token": config.auth_token
        }
    }
    listen_str = json.dumps(listen)
    ws.send(listen_str)

# Pinging keeps the WebSocket connection alive
def ping_worker(ws):
    while True:
        ping(ws)
        time.sleep(60 * 4) # 4 minutes (must be less than 5 minutes)

def ping(ws):
    ping_message = {
        "type": "PING"
    }
    ping = json.dumps(ping_message)
    ws.send(ping)
