from PyP100 import PyP110
from box import Box

from ..logger import build_logger

log = build_logger(".".join(["iot_controller", __name__]))


class P110Controller:
    def __init__(self, config: Box):
        self.obj = PyP110.P110(
            config.DEVICE_IP, config.DEVICE_USER, config.DEVICE_PASSWORD
        )
        self.obj.handshake()
        self.obj.login()
        log.info(f"P110 controller created: {self.obj=}")

    def on(self):
        # TODO: add check for status to confirm is actually on?
        self.obj.turnOn()
        log.info(f"Turned on: {self.obj=}")
        return None

    def off(self):
        self.obj.turnOff()
        log.info(f"Turned off: {self.obj=}")
        return None

    def usage(self):
        return self.obj.getEnergyUsage()

    def status(self):
        return self.obj.getDeviceInfo()
