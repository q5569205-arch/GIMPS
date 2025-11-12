import subprocess
from keep_alive import keep_alive

keep_alive()

try:
  subprocess.run(["./mprime","-m"])
except:
  subprocess.run(["chmod","777","./mprime"])
  subprocess.run(["./mprime", "-m"])
