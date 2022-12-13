from os import getenv

from .settings import *


SECRET_KEY = getenv("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = ["*"]
