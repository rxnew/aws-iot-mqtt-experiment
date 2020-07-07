```bash
docker-compose exec sub tc qdisc add dev eth0 root tbf rate 1kbit burst 0.01kb latency 70ms
```
