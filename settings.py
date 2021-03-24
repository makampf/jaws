from environs import Env

env = Env()
env.read_env()

LOG_LEVEL = env.str("LOG_LEVEL", default="INFO")
WEBSITE_URL = env.str("WEBSITE_URL", default="http://wetter.com")
ELEMENT_ID = env.str("ELEMENT_ID", default="cmp-btn-accept")
POLL_INTERVAL = env.int("POLL_INTERVAL", default="5")
