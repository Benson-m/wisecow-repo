import subprocess
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename="backup.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Variables
SOURCE_DIRECTORY = "/path/to/source_directory"
REMOTE_USER = "username"
REMOTE_HOST = "remote.host.com"
REMOTE_DIRECTORY = "/path/to/remote_directory"

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} - {message}"
    print(log_message)
    logging.info(log_message)

def perform_backup():
    command = ["rsync", "-avz", SOURCE_DIRECTORY, f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIRECTORY}"]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        log_message("Backup successful")
        log_message(result.stdout)
    except subprocess.CalledProcessError as e:
        log_message("Backup failed")
        log_message(e.stderr)

if __name__ == "_main_":
    perform_backup()