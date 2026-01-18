import logging
import json
from datetime import datetime
from config import dlp_settings as settings

class JsonAuditFormatter(logging.Formatter):
    def format(self, record):
        payload = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "event": record.getMessage()
        }
        if hasattr(record, "context"):
            payload.update(record.context)
        return json.dumps(payload)

def initialize_logger():
    logger = logging.getLogger("EnterpriseDLP")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(settings.AUDIT_LOG_FILE)
    file_handler.setFormatter(JsonAuditFormatter())

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    )

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

def record_event(event_name, context, severity="INFO"):
    logger = logging.getLogger("EnterpriseDLP")
    extra = {"context": {"event_type": event_name, **context}}

    if severity == "HIGH":
        logger.critical(event_name, extra=extra)
    elif severity == "MEDIUM":
        logger.warning(event_name, extra=extra)
    else:
        logger.info(event_name, extra=extra)
