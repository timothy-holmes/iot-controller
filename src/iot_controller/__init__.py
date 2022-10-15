__version__ = "0.1.0"

from fastapi import FastAPI
from ..logger import log

app = FastAPI()
log.info("App started")

from .routes import app

log.info("Routes loaded")
