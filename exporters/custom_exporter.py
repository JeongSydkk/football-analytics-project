# exporters/custom_exporter.py
from prometheus_client import start_http_server, Gauge
import time, random

temperature = Gauge("random_temperature_celsius", "Random temperature value")
humidity = Gauge("random_humidity_percent", "Random humidity value")

if __name__ == "__main__":
    print("✅ Custom exporter started on port 8000")
    start_http_server(8000)
    while True:
        temperature.set(random.uniform(18, 30))
        humidity.set(random.uniform(40, 70))
        time.sleep(5)
