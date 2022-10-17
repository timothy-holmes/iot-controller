from box import Box
from ..logger import log

config: Box = Box.from_json(filename="./config/config.json")

log.info('Config loaded')
