# MQTT Test

## Quick Start

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
