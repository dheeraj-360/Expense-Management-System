import logging

# create a custom Logger

def setup_logging(name, log_file = "server.log", level = logging.DEBUG):
    logger = logging.getLogger(name)

    # Configure a Custom Logger

    logger.setLevel(level)
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger