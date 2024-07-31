import psutil
import logging
import time

# Set up logging
logging.basicConfig(filename="system_health.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

def log_message(message):
    print(message)
    logging.info(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_message(f"High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        log_message(f"High Memory usage detected: {memory.percent}%")

def check_disk_usage():
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        log_message(f"Low Disk space detected: {disk.percent}% used")

def check_running_processes():
    processes = len(psutil.pids())
    log_message(f"Number of running processes: {processes}")

def monitor_system():
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_running_processes()
        # Check every 60 seconds
        time.sleep(60)

if __name__ == "_main_":
    monitor_system()