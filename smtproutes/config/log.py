import logging
from logging.handlers import RotatingFileHandler

_logger_initialized = False

def _initialize_logger():
    global _logger_initialized
    
    log_name = 'smtproutes'
    logger = logging.getLogger( log_name )

    handler = RotatingFileHandler(
        '/var/log/%s.log' % log_name,
        maxBytes=10485760,
        backupCount=3
    )
    logger.addHandler(handler)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    
    _logger_initialized = True

if not _logger_initialized:
    _initialize_logger()