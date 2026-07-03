import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# === HIER ANPASSEN ===
SCRIPT = os.path.join(BASE_DIR, "task_0187_f.py")
ARGS = ["-1", "0"]
TIMEOUT = 5
# =====================

RUN_TARGET = os.path.join(BASE_DIR, "_run_target.py")

try:
    result = subprocess.run(
        [sys.executable, RUN_TARGET, SCRIPT, *ARGS],
        timeout=TIMEOUT
    )

    if result.returncode == 0:
        print("Finished")
    else:
        print("Error")

except subprocess.TimeoutExpired:
    print("Timeout")