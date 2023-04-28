import os

class Config:
    API_ID = int(os.getenv("API_ID", 28906041))
    API_HASH = os.getenv("API_HASH", 'a07f71267d427ee069123c7eeb20e983')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '6116921113:AAFb3CzeN2gpVUhFKiCb2-LWY_nn3Yx3EI8')
