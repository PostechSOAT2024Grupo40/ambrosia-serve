FROM python:3.11-slim-bookworm

RUN apt-get update \
    && apt-get --no-install-recommends install -y build-essential libpq-dev python3-dev \
    && apt-get clean

COPY --from=ghcr.io/astral-sh/uv:0.4.16 /uv /uvx /bin/

WORKDIR /app

COPY . /app

RUN uv sync --frozen

EXPOSE 8000

ENTRYPOINT ["uv", "run", "main.py"]
