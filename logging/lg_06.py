import logging


# Instantiate a custom logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create handler to output to stdout
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.ERROR)
c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)

# Create handler to output to file
f_handler = logging.FileHandler("log", mode="w")
f_handler.setLevel(logging.DEBUG)
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
f_handler.setFormatter(f_format)
logger.addHandler(f_handler)

# Use the custom logger to log events
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")