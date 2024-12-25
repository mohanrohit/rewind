# everything like production, except the environment-specific flags
from .production import *

ENV = "development"

DEBUG = True
DEVELOPMENT = True
TESTING = False
