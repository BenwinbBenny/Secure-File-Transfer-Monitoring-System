class EventMapper:
    @staticmethod
    def map(event):
        return {
            "created": "FILE_CREATED",
            "modified": "FILE_MODIFIED",
            "deleted": "FILE_DELETED",
            "moved": "FILE_MOVED"
        }.get(event.event_type, "UNKNOWN_EVENT")
