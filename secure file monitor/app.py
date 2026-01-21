import time
from config import dlp_settings as settings
from core.audit_logger import initialize_logger, record_event
from core.filesystem_watcher import FileSystemWatcher

def main():
    initialize_logger()
    record_event("SYSTEM_STARTUP", {"monitoring": settings.MONITORED_DIRECTORY})

    watcher = FileSystemWatcher(settings.MONITORED_DIRECTORY)
    watcher.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        watcher.stop()
        record_event("SYSTEM_SHUTDOWN", {}

if __name__ == "__main__":
    main()

