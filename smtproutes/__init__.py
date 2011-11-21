from smtp_route import SMTPRoute
from contact import Contact
from routing_exception import RoutingException

import logging
from logging.handlers import RotatingFileHandler

def _create_logger():
    log_name = '/var/log/smtproutes.log'
    logger = logging.getLogger( log_name )
    logger.setLevel(logging.DEBUG)
    handler = RotatingFileHandler(
        log_name, 
        maxBytes=10485760,
        backupCount=3
    )
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = _create_logger()