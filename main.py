import sys

import uvicorn
from loguru import logger

from src.api.presentation.http import http  # noqa

logger.add(sys.stdout, enqueue=True)

if __name__ == "__main__":
    uvicorn.run("src.api.presentation.http:http.app", host="0.0.0.0", port=8000, reload=True)
