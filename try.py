import logging

# Crete and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="C:\\Users\\tahay\Desktop\\python-logging-try-area\\try.log", 
                    level = logging.DEBUG,
                    format = LOG_FORMAT)
logger = logging.getLogger()

# Test the logger
logger.info("Second message.")