from .config import config
from .p110 import P110Controller
from .logic import Logic
from ..logger import log
from . import app

logic = Logic(config.systems.raelia_heater) # TODO: BusinessLogicFactory()
raelia_heater = P110Controller(config=config.systems.raelia_heater.devices.P110)

# System
@app.get("/system/{state}")
def change_system_state(state: str):
    """
    Set system on or off.
    """
    if state == 'on' or state == 'off':
        logic.state = (state == 'on')
    else:
        return 'Invalid system state command'

# Shelly H&T receiver
@app.get("/shelly/ht")
def receive_ht(hum: int, temp: float, id: str):
    """
    Receive data from Shelly H&T device as query string.
    eg. hum=56&temp=19.00&id=shellyht-6BB646
    
    Prompts action according to business logic.
    """
    if not id or not id == config.systems.raelia_heater.devices.ht.DEVICE_ID:
        return 'Unknown device ID'
    
    log.info(f"New sensor reading {id=}: {temp=}")

    decision = logic.make_decision(temp)
    if decision == 'turn_on': 
        result = turn_on()
    elif decision == 'turn_off': 
        result = turn_off()
    else:
        result = None
    
    log.info(f"Decision {result=}")
    return result

# P110 controller
@app.get("/on")
def turn_on():
    log.info("GET /on")
    return raelia_heater.on()

@app.get("/off")
def turn_off():
    log.info("GET /off")
    return raelia_heater.off()

@app.get("/status")
def get_status():
    log.info("GET /status")
    return raelia_heater.status()

# IoT Controller
@app.get("/health")
def health_check():
    log.info("GET /health")
    return {"status": "OK"}

log.info("Routes loaded")
