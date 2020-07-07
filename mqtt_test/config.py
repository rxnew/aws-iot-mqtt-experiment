#!/usr/bin/env python
# coding: utf-8
import os.path
from os.path import join

from dotenv import load_dotenv

basedir = join(os.path.abspath(os.path.dirname(__file__)), "../")
dotenv_path = join(basedir, 'conf/.env')
load_dotenv(dotenv_path)

# AWS IoT
AWS_IOT_HOST = os.environ.get("AWS_IOT_HOST")
AWS_IOT_PORT = os.environ.get("AWS_IOT_PORT")
AWS_IOT_ROOTCA = os.environ.get("AWS_IOT_ROOTCA")
AWS_IOT_CERTIFICATE = os.environ.get("AWS_IOT_CERTIFICATE")
AWS_IOT_PRICATE_KEY = os.environ.get("AWS_IOT_PRICATE_KEY")
AWS_IOT_PUBLISH_KEY = os.environ.get("AWS_IOT_PUBLISH_KEY")

# MQTT
MQTT_HOST = os.environ.get("MQTT_HOST")
MQTT_PORT = os.environ.get("MQTT_PORT")
MQTT_KEEPALIVE = os.environ.get("MQTT_KEEPALIVE")
