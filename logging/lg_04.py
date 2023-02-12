import logging


"""
Configuring the logger is no longer possible after 
calling one of the following methods:

- logging.debug()
- logging.info()
- logging.warning()
- logging.error()
- logging.critical()

This is because these methods internally call the 
logging.basicConfig() method with default parameter values.
"""

# Use the default logger to log events
logging.warning("This is a warning message")

# Configure the default logger
logging.basicConfig(format="%(name)s - %(levelname)s : %(message)s")