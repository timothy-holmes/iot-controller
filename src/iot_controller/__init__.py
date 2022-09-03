__version__ = "0.1.0"

import uvicorn
from .routes import app
from .config import config


def main():
    uvicorn.run(
        app, host="0.0.0.0", port=config.UVICORN_PORT, log_level="debug", reload=True
    )
