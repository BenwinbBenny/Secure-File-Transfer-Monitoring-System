import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from core.event_mapper import EventMapper
from core.sensitivity_detector import SensitivityDetector
from core.hash_verifier import HashVerifier
from core.policy_evaluator import PolicyEvaluator
from core.alert_dispatcher import AlertDispatcher
from core.audit_logger import record_event

class DLPEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return

        event_name = EventMapper.map(event)
        file_path = event.src_path

        confidential, reason = SensitivityDetector.analyze(file_path)
        file_hash = HashVerifier.generate_sha256(file_path) if os.path.exists(file_path) else None

        context = {
            "file": file_path,
            "confidential": confidential,
            "classification": reason,
            "hash": file_hash
        }

        if event_name == "FILE_MOVED":
            status, msg, severity = PolicyEvaluator.evaluate_transfer(
                event.src_path, event.dest_path, confidential
            )
            context["destination"] = event.dest_path

            if status != "PERMITTED":
                AlertDispatcher.dispatch(severity, msg, context)
            else:
                record_event(event_name, context)
        else:
            if confidential and event_name == "FILE_DELETED":
                AlertDispatcher.dispatch("MEDIUM", "Confidential file deleted", context)
            else:
                record_event(event_name, context)

class FileSystemWatcher:
    def __init__(self, directory):
        self.observer = Observer()
        self.handler = DLPEventHandler()
        self.directory = directory

    def start(self):
        self.observer.schedule(self.handler, self.directory, recursive=True)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()
