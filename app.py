from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response
from prometheus_client import Counter, Gauge, Histogram, generate_latest, CONTENT_TYPE_LATEST
from prometheus_fastapi_instrumentator import Instrumentator
import random
import time

app = FastAPI()

# ---------------------------------------------------------------------
# Custom Metrics
# ---------------------------------------------------------------------

# Track total requests by method, endpoint, and status
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Count of requests by method, endpoint and status code",
    ["method", "endpoint", "status"]
)

# Latency per endpoint
REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request latency in seconds",
    ["endpoint"]
)

# Gauge for requests currently being processed
IN_PROGRESS = Gauge(
    "app_inprogress_requests",
    "Requests currently being processed"
)

# Track total errors
ERROR_COUNTER = Counter(
    "app_errors_total",
    "Total number of errors in the application"
)

# ---------------------------------------------------------------------
# Middleware to record metrics for all requests
# ---------------------------------------------------------------------
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    IN_PROGRESS.inc()
    start_time = time.time()

    try:
        response = await call_next(request)
        status = response.status_code
    except Exception:
        status = 500
        ERROR_COUNTER.inc()
        IN_PROGRESS.dec()
        raise

    latency = time.time() - start_time

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        status=status
    ).inc()

    REQUEST_LATENCY.labels(endpoint=request.url.path).observe(latency)

    IN_PROGRESS.dec()
    return response

# ---------------------------------------------------------------------
# Application Endpoints
# ---------------------------------------------------------------------

@app.get("/")
def home():
    # simulate work
    time.sleep(random.uniform(0.01, 1.5))
    return {"message": "Hello, world!"}

@app.get("/error")
def force_error():
    ERROR_COUNTER.inc()
    raise HTTPException(status_code=500, detail="Forced internal server error.")

@app.get("/divide-by-zero")
def divide_zero():
    try:
        1 / 0
    except ZeroDivisionError:
        ERROR_COUNTER.inc()
        raise HTTPException(status_code=500, detail="Division by zero error.")

# ---------------------------------------------------------------------
# Prometheus Metrics Endpoint
# ---------------------------------------------------------------------

@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)

# ---------------------------------------------------------------------
# Automatic instrumentation
# ---------------------------------------------------------------------

Instrumentator().instrument(app).expose(app)
