from PyP100 import PyP110
from box import Box

from ..logger import log


class P110Controller:
    def __init__(self, config: Box):
        self.config = config

    def _authenticate(self):
        try:
            _ = self.obj.getDeviceInfo()
        except Exception as e1:
            e = f"P110 Connection Error (L1): {e1}"
            log.error(e)
            try:
                self.obj = PyP110.P110(
                    self.config.DEVICE_IP, 
                    self.config.DEVICE_USER, 
                    self.config.DEVICE_PASSWORD
                )
                self.obj.handshake()
                self.obj.login()
            except Exception as e2:
                e = f"P110 Authentication Error (L2): {e2}"
                log.error(e)
            try:
                _ = self.obj.getDeviceInfo()
            except Exception as e3:
                e = f"P110 Authentication Failed (L3): {e3}"
                log.error(e)

    def action(self,action_str: str) -> str:
        allowed_methods = [
            'turnOn',
            'turnOff'
            'getDeviceInfo',
            'getEnergyUsage'
        ]
        if not action_str in allowed_methods:
            return 'Method not allowed'
        try:
            return getattr(self.obj,action_str)()
        except Exception as e1:
            self._authenticate()
            return getattr(self.obj,action_str)()