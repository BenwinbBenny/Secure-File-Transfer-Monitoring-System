import os
import time
import shutil
from config import dlp_settings as settings

target_file = os.path.join(
    settings.SECURE_STORAGE,
    "LuminaCore_FY26_Market_Analysis.docx"
)

with open(target_file, "w") as f:
    f.write("CONFIDENTIAL ENTERPRISE DATA")

time.sleep(2)

with open(target_file, "a") as f:
    f.write("\nUpdated financial projections")

time.sleep(2)

shutil.copy2(
    target_file,
    os.path.join(settings.EXTERNAL_MEDIA, os.path.basename(target_file))
)


