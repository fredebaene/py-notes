import logging


# Configure the default logger
logging.basicConfig(level=logging.DEBUG)

# Use the default logger to log events
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")