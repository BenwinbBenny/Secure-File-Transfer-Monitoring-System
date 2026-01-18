import os
from config import dlp_settings as settings

class PolicyEvaluator:
    @staticmethod
    def evaluate_transfer(source, destination, is_confidential):
        destination_path = os.path.abspath(destination)

        if is_confidential and settings.EXTERNAL_MEDIA in destination_path:
            return "BLOCKED", "Confidential data transferred to external media", "HIGH"

        if settings.EXTERNAL_MEDIA in destination_path:
            return "LOGGED", "File transferred to external media", "LOW"

        return "PERMITTED", "Operation allowed", "INFO"
