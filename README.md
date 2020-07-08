# MQTT Test

サブスクライバに対して帯域制御を行う。

```bash
docker-compose exec pub tc qdisc add dev eth0 root tbf rate 1kbit burst 0.01kb latency 70ms
```

サブスクライバに対するトラフィック制御を解除する。

```bash
docker-compose exec pub tc qdisc del dev eth0 root
```
