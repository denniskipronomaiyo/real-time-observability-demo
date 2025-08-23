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

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/real-time-observability-demo.git
cd real-time-observability-demo
