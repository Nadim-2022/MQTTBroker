import logging
import asyncio
import os
from amqtt.broker import Broker

logger = logging.getLogger(__name__)

config = {
    "listeners": {
        "default": {
            "type": "tcp",
            "bind": "0.0.0.0:1884",
        },
        "ws-mqtt": {
            "type": "ws",
            "bind": '0.0.0.0:8884'  # Listen on port 9001 for WebSocket connections

        },
    },
    "sys_interval": 10,
    "auth": {
        "allow-anonymous": True,
    },
    "topic-check": {"enabled": True, "plugins": ["topic_taboo"]}, # enable topic access control
}

broker = Broker(config)


async def test_coro():
    await broker.start()
    # await asyncio.sleep(5)
    # await broker.shutdown()


if __name__ == "__main__":
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"
    # formatter = "%(asctime)s :: %(levelname)s :: %(message)s"
    logging.basicConfig(level=logging.INFO, format=formatter)
    asyncio.get_event_loop().run_until_complete(test_coro())
    asyncio.get_event_loop().run_forever()