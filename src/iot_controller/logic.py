from box import Box

from .config import config
from ..logger import log

class Logic:
    def __init__(self, system: Box):
        # self.sensor: str = config.systems[system].devices.ht
        # self.actuator: str = config.systems[system].devices.P110
        self.set_point: float = system.set_point
        self.last_temp = None
        self.state: bool = False

    def make_decision(self, temp: float):
        """
        TODO: boolean that shit
        Decision matrix:
            temp > set_point --> off
            temp < set_point --> on
            temp = set_point --> trend is up --> off
            temp = set_point --> trend is down --> on
        """
        if self.state: # True
            if temp < self.set_point:
                decision = True
            elif temp > self.set_point:
                decision = False
            else:
                if self.last_temp and temp < self.last_temp:
                    decision = True
                else:
                    decision = False
        else: # False or None
            decision = False

        self.last_temp = temp
        return decision