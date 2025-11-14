# Real-Time Observability Demo 🚀

A simple Python **FastAPI** application that exposes **custom Prometheus metrics** (counters, gauges, histograms) for real-time observability and alerting.

This project is part of a hands-on journey to learn **observability, monitoring, and alerting** by building from scratch.

---

## 📌 Features
- Exposes a REST API (`/`) that simulates requests  
- Tracks request **count, latency, and in-progress requests**  
- Exposes Prometheus-compatible metrics at `/metrics`  
- Built with **FastAPI + prometheus-client**  

---

## ⚡ Getting Started

1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/real-time-observability-demo.git
cd real-time-observability-demo
```

2️⃣ Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the app
uvicorn app:app --reload --host 0.0.0.0 --port 8000

🔍 Endpoints
| Endpoint   | Description                        |
| ---------- | ---------------------------------- |
| `/`        | Simple API returning JSON response |
| `/metrics` | Prometheus metrics endpoint        |

Example metrics exposed:
app_request_count Total request count
TYPE app_request_count counter
app_request_count{method="GET",endpoint="/"} 12.0

## ⚡ Getting Started with prometheus

🛠️ Step 1: Create prometheus.yml

🛠️ Step 2: Install Prometheus

If you have Docker installed:

docker run -p 9090:9090 -v %cd%\prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus

## ⚡ Getting Started with Grafana

🛠️ Step 1: Install Grafana

docker run -d -p 3000:3000 --name grafana `
  -e "GF_SECURITY_ADMIN_USER='' " `
  -e "GF_SECURITY_ADMIN_PASSWORD='' " `
  grafana/grafana

🛠️ Step 2: Access Grafana

Open http://localhost:3000
 in your browser and log in.

🛠️ Step 3:  Add Prometheus as a Data Source

Go to Connections → Data sources → Add data source

Select Prometheus

In the URL field, enter: http://host.docker.internal:9090