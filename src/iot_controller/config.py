import json

from box import Box

from ..logger import log

# load config json to Box
config: Box = Box.from_json(filename="./config/config.json", box_dots=True)

# merge secrets into config box
with open("./config/secrets.json","r") as secrets_json:
    s = json.load(secrets_json)

for k,v in s.items():
    config[k] = v

log.info('Config loaded')
