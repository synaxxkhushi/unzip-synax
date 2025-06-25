import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6909770226:AAE6bS7UMt314uteUI8XucLOaFgE4yHyJ6w")
    API_ID = int(os.environ.get("API_ID", "14050586"))
    API_HASH = os.environ.get("API_HASH", "42a60d9c657b106370c79bb0a8ac560c")
    
    
