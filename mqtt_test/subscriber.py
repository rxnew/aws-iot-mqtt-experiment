import json
import time
import uuid
from datetime import datetime, timedelta, timezone

from . import aws
from .config import MQTT_TOPIC, MQTT_QOS

_tz = timezone(timedelta(hours=+9), 'JST')


def on_message(client, userdata, message):
    data = json.loads(str(message.payload.decode('utf-8')))
    id = data['id']
    recv_ts = time.time_ns()
    sent_ts = data['timestamp']
    dt = (recv_ts - sent_ts) / 1000000000
    recv_ts_s = datetime.fromtimestamp(recv_ts / 1000000000).astimezone(_tz).isoformat()
    print('[%s] id:%d delay:%.6f' % (recv_ts_s, id, dt))


def main():
    client = aws.new_mqtt_client(str(uuid.uuid4()))
    client.connect()
    client.subscribe(MQTT_TOPIC, MQTT_QOS, on_message)
    while True:
        time.sleep(5)


if __name__ == '__main__':
    main()
