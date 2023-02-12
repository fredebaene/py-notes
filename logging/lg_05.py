import logging


# Configure the default logger
logging.basicConfig(level=logging.DEBUG)

# Initialize user
name = "John"

# Log the user logging in
logging.info(f"{name} logged in")