# MQTT Test

## Quick Start

Download a device certificate from AWS IoT to `cert` directory with reference to [an official document](https://docs.aws.amazon.com/iot/latest/developerguide/create-device-certificate.html).

Create `.env` file with reference to `.env.sample`.

Start a publisher:

```bash
docker-compose up pub
```

Start a subscriber:

```bash
docker-compose up sub
```

## Experiment

Provides bandwidth control to the publisher:

```bash
docker-compose exec pub tc qdisc add dev eth0 root tbf rate 1kbit burst 0.01kb latency 70ms
```

Remove traffic control to the publisher:

```bash
docker-compose exec pub tc qdisc del dev eth0 root
```
