"""Logging configuration for the cell simulation."""

import logging
import os

def setup_logger():
    """Set up the logger with custom formatting."""
    logger = logging.getLogger('cell_simulation')
    logger.setLevel(logging.DEBUG)
    logger.propagate = False  # Prevent log messages from being passed to the root logger

    # Remove all handlers associated with the logger
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # File handler only
    log_dir = os.path.join(os.path.dirname(__file__), '..')
    log_path = os.path.abspath(os.path.join(log_dir, 'cell_simulation.log'))
    file_handler = logging.FileHandler(log_path, mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# Create logger instance
logger = setup_logger()
