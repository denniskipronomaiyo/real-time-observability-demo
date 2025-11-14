# ──────────────────────────────────────────
#  Variables
# ──────────────────────────────────────────
COMPOSE=docker-compose
PY=python

# ──────────────────────────────────────────
#  Local Development
# ──────────────────────────────────────────
run:
	uvicorn app:app --reload --host 0.0.0.0 --port 8000

install:
	pip install -r requirements.txt

lint:
	flake8 .

# ──────────────────────────────────────────
#  Docker Build & Services
# ──────────────────────────────────────────
build:
	$(COMPOSE) build

up:
	$(COMPOSE) up --build

down:
	$(COMPOSE) down

restart:
	$(COMPOSE) down && $(COMPOSE) up --build

logs:
	$(COMPOSE) logs -f

# ──────────────────────────────────────────
#  Cleanup
# ──────────────────────────────────────────
clean:
	docker system prune -f
