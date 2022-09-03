from fastapi import FastAPI

from .config import config
from .p110 import P110Controller
from ..logger import build_logger

log = build_logger(".".join(["iot_controller", __name__]))

app = FastAPI()
log.info("App started")


@app.get("/on")
def turn_on():
    log.info("GET /on")
    raelia_heater = P110Controller(config=config.devices.raelia_heater)
    return raelia_heater.on()


@app.get("/off")
def turn_off():
    log.info("GET /off")
    raelia_heater = P110Controller(config=config.devices.raelia_heater)
    return raelia_heater.off()


log.info("Routes loaded")
