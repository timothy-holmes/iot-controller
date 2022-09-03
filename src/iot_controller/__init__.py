__version__ = "0.1.0"

from fastapi import FastAPI
from ..logger import build_logger

log = build_logger(".".join(["iot_controller", __name__]))

app = FastAPI()
log.info("App started")

from .routes import app

log.info("Routes loaded")
