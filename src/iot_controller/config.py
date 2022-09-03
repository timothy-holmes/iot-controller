from box import Box
from ..logger import build_logger

log = build_logger(".".join(["iot_controller", __name__]))

config: Box = Box.from_json(filename="./config/config.json")
