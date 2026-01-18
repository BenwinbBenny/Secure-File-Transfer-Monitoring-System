# Secure-File-Transfer-Monitoring-System

## 📌 Overview

The **Secure-File-Transfer-Monitoring-System** is a Python-based Data Loss Prevention (DLP) solution designed to monitor file system activities, detect sensitive data, evaluate transfer policies, and generate audit logs or alerts based on predefined security rules.

This system continuously watches a directory for file events (create, modify, delete, move), evaluates whether files are confidential, checks transfer destinations, and enforces security policies such as blocking or alerting on unauthorized transfers to external media.

---

## 🧩 Key Features

- 📂 **Real-time File System Monitoring**
- 🔍 **Confidential Data Detection**
- 🛡️ **Policy-Based Transfer Evaluation**
- 🚨 **Alert Dispatching with Severity Levels**
- 🧾 **Centralized Audit Logging**
- 🔐 **SHA-256 File Integrity Verification**

---

## 🏗️ System Architecture
```

+----------------------+
| FileSystemWatcher    |
| (watchdog.Observer)  |
+----------+-----------+
           |
           v
+----------------------+
| DLPEventHandler      |
+----------+-----------+
           |
           v
+----------------------+        +--------------------+
| SensitivityDetector  |        | PolicyEvaluator   |
+----------+-----------+        +--------------------+
           |                            |
           +------------+---------------+
                        |
                        v
               +------------------+
               | AlertDispatcher  |
               | / Audit Logger   |
               +------------------+

```
---

## 📁 Module Documentation

### 1️⃣ FileSystemWatcher

**Purpose:**  
Monitors a specified directory for file system events using the `watchdog` library.

**Key Responsibilities:**
- Initializes an observer and event handler  
- Starts and stops directory monitoring  

```python
class FileSystemWatcher:
    def init(self, directory):
        self.observer = Observer()
        self.handler = DLPEventHandler()
        self.directory = directory
```
### 2️⃣ EventMapper

**Purpose:**  
Maps low-level file system events to standardized internal event names.

| OS Event Type | Internal Event |
|--------------|----------------|
| created      | FILE_CREATED   |
| modified     | FILE_MODIFIED  |
| deleted      | FILE_DELETED   |
| moved        | FILE_MOVED     |

---

### 3️⃣ SensitivityDetector

**Purpose:**  
Determines whether a file is confidential based on:

- File extensions  
- Sensitive keywords in filenames  

**Configuration Driven:**  
Uses values from `config.dlp_settings`

- `CONFIDENTIAL_EXTENSIONS`  
- `CONFIDENTIAL_KEYWORDS`  

**Return Value:**
```text
(bool is_confidential, str reason)
```
### 4️⃣ PolicyEvaluator

**Purpose:**  
Evaluates whether a file transfer should be:

- **PERMITTED**
- **LOGGED**
- **BLOCKED**

**Decision Factors:**
- Confidentiality of the file  
- Destination path (e.g., external media)  

**Severity Levels:**
- INFO  
- LOW  
- HIGH  

---

### 5️⃣ HashVerifier

**Purpose:**  
Generates a SHA-256 hash for file integrity validation.

**Use Cases:**
- Detect file tampering  
- Maintain audit trail integrity

### 6️⃣ AlertDispatcher & Audit Logger

**Purpose:**
- Sends alerts for policy violations  
- Records all system and file events  

**Behavior:**
- BLOCKED or suspicious actions → **Alerts**  
- Allowed actions → **Event logging**

---

## 🔄 Event Processing Logic

1. File system event occurs  
2. Event is mapped using `EventMapper`  
3. File sensitivity is analyzed  
4. Transfer policy is evaluated  
5. Based on the result:
   - Alert is dispatched **OR**
   - Event is logged  

## 🧪 Simulation Script

The included simulation demonstrates:

- Creating a confidential document  
- Modifying the file  
- Copying it to external media  
- Triggering alerts for policy violations  

```python
shutil.copy2(
    target_file,
    os.path.join(settings.EXTERNAL_MEDIA, os.path.basename(target_file))
)
```
## 🚀 Application Entry Point

```python
def main():
    initialize_logger()
    record_event("SYSTEM_STARTUP", {"monitoring": settings.MONITORED_DIRECTORY})

    watcher = FileSystemWatcher(settings.MONITORED_DIRECTORY)
    watcher.start()
```
**Runtime Behavior:**
- Initializes logging  
- Starts monitoring  
- Gracefully shuts down on `Ctrl+C`

## ⚙️ Configuration (`config/dlp_settings.py`)

Typical settings include:

- `MONITORED_DIRECTORY`  
- `SECURE_STORAGE`  
- `EXTERNAL_MEDIA`  
- `CONFIDENTIAL_EXTENSIONS`  
- `CONFIDENTIAL_KEYWORDS`  

---

## 🛠️ Dependencies

- Python 3.x  
- watchdog  
- hashlib  
- shutil  
- os  
- time  

Install `watchdog`:
```bash
pip install watchdog
```
## 🔐 Security Use Cases

- Prevent confidential file leaks to USB / external drives  
- Audit file access and modification  
- Enforce enterprise data protection policies  
- Detect suspicious deletion of sensitive files  

---

## 📜 License

This project is intended for educational and enterprise security research purposes.  
Customize and extend according to organizational security requirements.

---

## ✨ Future Enhancements

- Email / SIEM alert integration  
- Content-based file scanning  
- Role-based access controls  
- Encrypted secure storage  
- Cross-platform support  

---

**Secure your data. Monitor intelligently. Act decisively. 🔒**

