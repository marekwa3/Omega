import logging

logging.basicConfig(
    filename='../data/log.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [%(category)s] %(message)s'
)

def log_Info(category, message):
    logging.info(message, extra={'category': category})

def log_Warning(category, message):
    logging.warning(message, extra={'category': category})

def log_Error(category, message):
    logging.error(message, extra={'category': category})
