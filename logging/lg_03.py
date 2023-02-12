import logging


# Configure the default logger
logging.basicConfig(
    level=logging.DEBUG,
    filename="log",
    filemode="w",
    format="%(name)s - %(levelname)s : %(message)s"
)

# Log an event
logging.warning("This is a warning message")