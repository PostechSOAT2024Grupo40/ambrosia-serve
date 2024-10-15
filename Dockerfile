FROM python:3.11-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.4.16 /uv /uvx /bin/

WORKDIR /app

COPY . /app

RUN uv sync --frozen

CMD ["uv", "run", "src/main.py"]
