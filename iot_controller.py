import uvicorn
from src.iot_controller.config import config

if __name__ == "__main__":
    uvicorn.run(
        "src.iot_controller:app",
        host="0.0.0.0",
        port=config.UVICORN_PORT,
        log_level="debug",
        reload=True,
    )
