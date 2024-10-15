import uvicorn

from src.api.presentation.http import http  # noqa

if __name__ == "__main__":
    uvicorn.run("src.api.presentation.http:http.app", host="127.0.0.1", port=8000, reload=True)
