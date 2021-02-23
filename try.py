import logging

# Crete and configure logger
logging.basicConfig(filename="C:\\Users\\tahay\Desktop\\python-logging-try-area\\try.log", level=logging.DEBUG)
logger = logging.getLogger()

# Test the logger
logger.info("Second message.")