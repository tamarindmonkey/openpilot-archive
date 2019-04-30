import time
import json
import threading
from common.basedir import BASEDIR

def phantom_thread():
  global data
  global high_frequency
  thread_interval = 5  # 12hz
  thread_start = time.time()
  while True:
    time.sleep(thread_interval)
    start = time.time()
    data = read_phantom()
    if data["status"]:
      thread_start = time.time()
      if high_frequency:
        thread_interval = 0.02  # 50hz for steering
      else:
        thread_interval = 0.2  # 5hz
    else:
      thread_interval = 5
    thread_interval = max(thread_interval - (time.time() - start), 0)  # rate keeper
    if (time.time() - thread_start) > (20*60):  # if car is on for more than 20 minutes without phantom activation, shut down thread
      break

def read_phantom():
  tmp = None
  try:
    with open(phantom_file, "r") as f:
      tmp = f.read()
      f.seek(0)
      return json.loads(f.read())
  except Exception,e:
    with open("/data/test_file.txt", "a") as f:
      f.write(str(e)+"\n"+tmp+"\n")
    return {"status": False}

high_frequency = False  # set to true from latcontrol, false for long control
data = {"status": False}
phantom_file = "/data/phantom.json"
if BASEDIR == "/data/openpilot":
  threading.Thread(target=phantom_thread).start()