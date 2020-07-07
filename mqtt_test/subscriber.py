import json
import time
import uuid
from datetime import datetime

from pytz import timezone

import aws


def on_message(client, userdata, message):
    data = json.loads(str(message.payload.decode('utf-8')))
    id = data['id']
    recv_ts = time.time()
    sent_ts = data['timestamp']
    dt = recv_ts - sent_ts
    recv_ts_s = datetime.fromtimestamp(recv_ts).astimezone(timezone('Asia/Tokyo'))
    sent_ts_s = datetime.fromtimestamp(sent_ts).astimezone(timezone('Asia/Tokyo'))
    print('%d,%s,%s,%.6f' % (id, sent_ts_s, recv_ts_s, dt))


def main():
    client = aws.new_mqtt_client(str(uuid.uuid4()))
    client.connect()
    client.subscribe('test/drive/experiment', 0, on_message)
    while True:
        time.sleep(5)


if __name__ == '__main__':
    main()
