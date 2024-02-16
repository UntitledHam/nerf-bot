import os.path
import tomllib

def init():
    with open("config.toml", "rb") as f:
        global config
        config = tomllib.load(f)