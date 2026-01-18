import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
REPORT_DIR = os.path.join(PROJECT_ROOT, "reports")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")

for directory in (LOG_DIR, REPORT_DIR, DATA_DIR):
    os.makedirs(directory, exist_ok=True)

MONITORED_DIRECTORY = os.path.join(DATA_DIR, "watched_area")
SECURE_STORAGE = os.path.join(MONITORED_DIRECTORY, "secure_storage")
EXTERNAL_MEDIA = os.path.join(MONITORED_DIRECTORY, "external_media")

os.makedirs(SECURE_STORAGE, exist_ok=True)
os.makedirs(EXTERNAL_MEDIA, exist_ok=True)

CONFIDENTIAL_EXTENSIONS = [".pdf", ".docx", ".xlsx", ".pem", ".key"]
CONFIDENTIAL_KEYWORDS = ["confidential", "secret", "salary", "budget"]

AUDIT_LOG_FILE = os.path.join(LOG_DIR, "dlp_audit.log")
