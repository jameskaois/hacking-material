"""
Safe educational demo: local-only keystroke logger in a focused GUI window.

- Captures key events only while the app's window is focused.
- Writes timestamps + key info to a local log file (keystrokes_local.log).
- No network activity, no global hooks, not stealthy.

Run in your lab VM with: python3 safe_keystroke_demo.py
"""

import tkinter as tk
from datetime import datetime
from pathlib import Path

LOGFILE = Path("keystrokes_local.log")

def log_key(event):
    # event.keysym: a readable name for the key pressed
    # event.char: the actual character (may be empty for special keys)
    timestamp = datetime.utcnow().isoformat() + "Z"
    entry = f"{timestamp}\tkeysym={event.keysym}\tchar={repr(event.char)}\n"
    # Append to local file (no network/don't send anywhere)
    with LOGFILE.open("a", encoding="utf-8") as f:
        f.write(entry)
    # Also update the GUI display (for demo/verification)
    txt.insert(tk.END, entry)
    txt.see(tk.END)

def on_focus_in(_):
    status_var.set("Window focused — capturing keys (local only)")

def on_focus_out(_):
    status_var.set("Window unfocused — not capturing keys")

def clear_log():
    LOGFILE.write_text("")  # truncate
    txt.delete("1.0", tk.END)

# --- Build GUI ---
root = tk.Tk()
root.title("Safe Keystroke Demo — Local Only")
root.geometry("700x400")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

status_var = tk.StringVar(value="Window unfocused — not capturing keys")
status = tk.Label(root, textvariable=status_var)
status.pack(side=tk.BOTTOM, fill=tk.X, padx=4, pady=4)

instructions = tk.Label(frame, text=(
    "Type in this window. Keys will be logged to 'keystrokes_local.log' "
    "and shown below. This captures only while this window has focus."
))
instructions.pack(anchor="w")

txt = tk.Text(frame, wrap=tk.NONE, height=18)
txt.pack(fill=tk.BOTH, expand=True)

btn_frame = tk.Frame(root)
btn_frame.pack(fill=tk.X, padx=8, pady=(0,8))
clear_btn = tk.Button(btn_frame, text="Clear log file & display", command=clear_log)
clear_btn.pack(side=tk.LEFT)

# Bind key events only while the window is focused:
root.bind("<Key>", log_key)
root.bind("<FocusIn>", on_focus_in)
root.bind("<FocusOut>", on_focus_out)

# Ensure the logfile exists
LOGFILE.touch(exist_ok=True)

root.mainloop()
