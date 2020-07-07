import json
import time
import uuid

from . import aws


def main():
    client = aws.new_mqtt_client(str(uuid.uuid4()))
    client.connect()

    i = 0
    while True:
        data = {
            'id': i,
            'timestamp': time.time(),
            'message': 'Message from 100',
        }
        payload = json.dumps(data)
        client.publishAsync('test/drive/experiment', payload, 0)
        time.sleep(1)
        i += 1


if __name__ == '__main__':
    main()
