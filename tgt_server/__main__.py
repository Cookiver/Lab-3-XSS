import uvicorn
from tgt_server.config import settings


if __name__ == "__main__":
    uvicorn.run("tgt_server:app", host=settings.api_host, port=settings.api_port, log_level=settings.api_log_level)
