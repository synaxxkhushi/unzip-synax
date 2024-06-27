import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6909770226:AAE6bS7UMt314uteUI8XucLOaFgE4yHyJ6w")
    API_ID = int(os.environ.get("API_ID", "24267726"))
    API_HASH = os.environ.get("API_HASH", "7500ba8248548cc3864bd033668f9a9a")
    
    
