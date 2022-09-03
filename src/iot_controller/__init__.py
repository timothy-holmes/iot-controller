__version__ = "0.1.0"

import uvicorn
from .config import config


def main():
    uvicorn.run(
        "src.iot_controller:app",
        host="0.0.0.0",
        port=config.UVICORN_PORT,
        log_level="debug",
        reload=True,
    )
