import subprocess
import time


# open Telegram
def open_telegram(path):
    time.sleep(1)
    return subprocess.Popen(path)