import time
import argparse
import requests
import random

URL = "http://localhost:8000/"

ERROR_URLS = [
    "http://localhost:8000/error",'http://localhost:8000/divide-by-zero']

def hit_error():
    try:
        r = requests.get(random.choice(ERROR_URLS))
        print(f"{r.status_code}")
    except Exception as e:
        print("ERROR:", e)

def hit():
    try:
        r = requests.get(URL)
        print(f"{r.status_code}")
    except Exception as e:
        print("ERROR:", e)

def constant(rps):
    interval = 1 / rps
    while True:
        hit()
        time.sleep(interval)

def bursty():
    while True:
        for _ in range(random.randint(10, 30)):
            hit()
            hit_error()
            time.sleep(random.uniform(0.01, 0.1))
        time.sleep(random.uniform(2, 5))

def ramp(max_rps):
    for rps in range(1, max_rps + 1):
        print("RPS:", rps)
        for _ in range(rps):
            hit()
            time.sleep(1 / rps)

    while True:
        hit()
        time.sleep(1 / max_rps)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["constant", "bursty", "ramp"], required=True)
    parser.add_argument("--rps", type=int, default=5)
    parser.add_argument("--max_rps", type=int, default=20)
    args = parser.parse_args()

    if args.mode == "constant":
        constant(args.rps)
    elif args.mode == "bursty":
        bursty()
    else:
        ramp(args.max_rps)
