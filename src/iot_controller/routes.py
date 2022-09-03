from .config import config
from .p110 import P110Controller
from ..logger import build_logger
from iot_controller import app

log = build_logger(".".join(["iot_controller", __name__]))


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


@app.get("/status")
def get_status():
    log.info("GET /status")
    raelia_heater = P110Controller(config=config.devices.raelia_heater)
    return raelia_heater.status()


log.info("Routes loaded")
