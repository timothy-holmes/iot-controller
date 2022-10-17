from PyP100 import PyP110
from box import Box

from ..logger import log


class P110Controller:
    def __init__(self, config: Box):
        self.obj = PyP110.P110(
            config.DEVICE_IP, config.DEVICE_USER, config.DEVICE_PASSWORD
        )
        log.info(f"P110 ({config.DEVICE_IP}) controller created: {self.obj=}")
        a = self.authenticate()
        if a:
            log.info(f"P110 ({config.DEVICE_IP}) controller authenticated")

    def authenticate(self):
        try:
            _ = self.obj.getDeviceInfo()
        except Exception as e1:
            e = f"P110 Connection Error: {e1}"
            log.error(e)
            try:
                self.obj.handshake()
                self.obj.login()
            except Exception as e2:
                e = f"P110 Authentication Error: {e2}"
                log.error(e)
            try:
                _ = self.obj.getDeviceInfo()
            except Exception as e3:
                e = f"P110 Authentication Failed: {e3}"
                log.error(e)

    def action(self,action_str: str) -> str:
        if action_str in dir(self):
            action_method = getattr(self, '_' + action_str)
            if callable(action_method):
                try:
                    result = action_method()
                except Exception as e1:
                    e = f"P110 Connection Error: {e1}"
                    log.error(e)
                    _ = self.authenticate()
                    _ = action_method()
                return action_str
            else:
                return 'Invalid method (not callable)'
        else:
            return 'Invalid method (does not exist)'

    def _on(self):
        # TODO: add check for status to confirm is actually on?
        self.obj.turnOn()
        log.info(f"Turned on: {self.obj=}")

    def _off(self):
        self.obj.turnOff()
        log.info(f"Turned off: {self.obj=}")

    def _usage(self):
        return self.obj.getEnergyUsage()

    def _status(self):
        return self.obj.getDeviceInfo()
