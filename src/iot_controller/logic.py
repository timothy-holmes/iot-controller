from .config import config

class Logic:
    def __init__(self, system: str):
        # self.sensor: str = config.system[system].devices.ht
        # self.actuator: str = config.system[system].devices.P110
        self.set_point: float = config.system[system].set_point
        self.last_temp = None

    def make_decision(self, temp):
        """
        TODO: boolean that shit
        Decision matrix:
            temp > set_point --> off
            temp < set_point --> on
            temp = set_point --> trend is up --> off
            temp = set_point --> trend is down --> on
        """
        if temp > self.set_point:
            decision = 'turn_off'
        elif temp < self.set_point:
            decision = 'turn_on'
        else:
            if temp > self.last_temp:
                decision = 'turn_off'
            else:
                decision = 'turn_on'

        self.last_temp = temp
        return decision