from .config import config
from .p110 import P110Controller
from .logic import Logic
from ..logger import log
from . import app

logic = Logic(config.systems.raelia_heater) # TODO: logic: dict[str, Logic] = BusinessLogicFactory(config.systems)
raelia_heater = P110Controller(config=config.systems.raelia_heater.devices.P110)

# System
@app.get("/system/toggle_state")
def change_system_state():
    """
    Set system on or off.
    """
    logic.state = not logic.state
    log.debug(f'{logic.state=}')

    if logic.state:
        raelia_heater.action('on')
        log.debug(f'{logic.state=}, heater=on')
    else:
        raelia_heater.action('off')
        log.debug(f'{logic.state=}, heater=off')

    return f'{logic.state=}'

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
    if decision:
        raelia_heater.action('on')
        return 'raelia_heater=on' 
    else:
        raelia_heater.action('off')
        return 'raelia_heater=off'

# P110 controller
@app.get("/p110/{action}")
def do_p110_action(action: str):
    return raelia_heater.action(action)

# IoT Controller
@app.get("/health")
def health_check():
    log.info("GET /health")
    return {"status": "OK"}

log.info("Routes loaded")
