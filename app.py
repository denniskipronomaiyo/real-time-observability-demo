from fastapi import FastAPI
from prometheus_client import Counter, Gauge, Histogram, generate_latest
from fastapi.responses import PlainTextResponse
import random
import time

app = FastAPI()

# --- Define Custom Metrics ---
REQUEST_COUNT = Counter(
    "app_request_count", "Total request count", ["method", "endpoint"]
)
REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds", "Request latency (seconds)", ["endpoint"]
)
IN_PROGRESS = Gauge("app_inprogress_requests", "Requests in progress")

# --- Endpoints ---
@app.get("/")
@IN_PROGRESS.track_inprogress()
def home():
    start_time = time.time()
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()

    # simulate work
    time.sleep(random.uniform(0.1, 0.5))

    latency = time.time() - start_time
    REQUEST_LATENCY.labels(endpoint="/").observe(latency)

    return {"message": "Hello, world!"}

# Prometheus metrics endpoint
@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest().decode("utf-8"))



