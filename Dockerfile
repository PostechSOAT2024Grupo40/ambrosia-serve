FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

RUN apt-get update \
    && apt-get --no-install-recommends install -y build-essential libpq-dev python3-dev \
    && apt-get clean

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1

ENV UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

COPY ./mock-payment-server /app/mock-payment-server
COPY ./src /app/src
COPY ./pyproject.toml /app
COPY ./uv.lock /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:$PATH"


EXPOSE 80

ENTRYPOINT []
CMD ["fastapi", "run", "--workers", "4", "--port", "80",  "src/api/presentation/http/http.py"]
