import os

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from requests import certs

from .config import (
    AWS_IOT_HOST, AWS_IOT_PORT, AWS_IOT_ROOTCA, AWS_IOT_CERTIFICATE, AWS_IOT_PRICATE_KEY,
)

ECS_CONTAINER_CREDENTIALS_HOST = '169.254.170.2'

IOT_SHADOW_TOPIC_FORMAT = '$aws/things/{}/shadow/{}'

_cert_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../cert/')


def get_iot_cert_credentials():
    ca_file_path = get_iot_root_ca()
    key_path = _cert_dir_path + AWS_IOT_PRICATE_KEY if AWS_IOT_PRICATE_KEY else ''
    cert_path = _cert_dir_path + AWS_IOT_CERTIFICATE if AWS_IOT_CERTIFICATE else ''
    return {
        'CAFilePath': ca_file_path,
        'KeyPath': key_path,
        'CertificatePath': cert_path,
    }


def get_iot_root_ca():
    if AWS_IOT_ROOTCA:
        return _cert_dir_path + AWS_IOT_ROOTCA
    return certs.where()


def get_iot_shadow_topic(thing_name, action):
    if len(action) > 1 and action.startswith('/'):
        action = action[1:]
    return IOT_SHADOW_TOPIC_FORMAT.format(thing_name, action)


def new_mqtt_client(client_id):
    if _use_x509_cert():
        client = _new_mqtt_client(client_id)
    else:
        client = _new_mqtt_client_over_ws(client_id)
    client.configureEndpoint(AWS_IOT_HOST, int(AWS_IOT_PORT))
    client.configureAutoReconnectBackoffTime(1, 32, 20)
    client.configureConnectDisconnectTimeout(10)  # 10 sec
    client.configureMQTTOperationTimeout(5)  # 5 sec
    client.onOnline = lambda: print('Changed MQTT connection status: online')
    client.onOffline = lambda: print('Changed MQTT connection status: offline')

    return client


def _new_mqtt_client(client_id):
    client = AWSIoTMQTTClient(client_id)
    credentials = get_iot_cert_credentials()
    client.configureCredentials(**credentials)
    return client


def _new_mqtt_client_over_ws(client_id):
    client = AWSIoTMQTTClient(client_id, useWebsocket=True)
    root_ca = get_iot_root_ca()
    client.configureCredentials(root_ca)
    return client


def _use_x509_cert():
    return AWS_IOT_PRICATE_KEY and AWS_IOT_CERTIFICATE
