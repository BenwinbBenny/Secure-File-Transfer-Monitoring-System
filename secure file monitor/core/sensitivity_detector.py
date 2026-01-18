import os
from config import dlp_settings as settings

class SensitivityDetector:
    @staticmethod
    def analyze(file_path):
        filename = os.path.basename(file_path).lower()
        extension = os.path.splitext(filename)[1]

        if extension in settings.CONFIDENTIAL_EXTENSIONS:
            return True, "Restricted file type"

        if any(keyword in filename for keyword in settings.CONFIDENTIAL_KEYWORDS):
            return True, "Sensitive keyword detected"

        return False, "Public file"
