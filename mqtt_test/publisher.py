import json
import time
import uuid
from datetime import datetime, timedelta, timezone

from . import aws
from .config import MQTT_TOPIC, MQTT_QOS, MQTT_PUBLISH_INTERVAL

_tz = timezone(timedelta(hours=+9), 'JST')


def main():
    client = aws.new_mqtt_client(str(uuid.uuid4()))
    client.connect()

    i = 0
    t = MQTT_PUBLISH_INTERVAL / 1000.0
    while True:
        send_ts = time.time_ns()
        send_ts_s = datetime.fromtimestamp(send_ts / 1000000000).astimezone(_tz).isoformat()
        data = {'id': i, 'timestamp': send_ts}
        payload = json.dumps(data)
        client.publish(MQTT_TOPIC, payload, MQTT_QOS)
        print('[%s] id:%d' % (send_ts_s, i))
        time.sleep(t)
        i += 1


if __name__ == '__main__':
    main()
