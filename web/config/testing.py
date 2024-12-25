# everything like production, except the environment-specific flags
from .production import *

ENV = "testing"

DEBUG = False
DEVELOPMENT = False
TESTING = True
