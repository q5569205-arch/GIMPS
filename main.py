import subprocess
import time
import uuid

from keep_alive import keep_alive

keep_alive()

subprocess.run(["chmod", "777", "./mprime"])
p = subprocess.Popen(["./mprime", "-m"], stdin=subprocess.PIPE)
time.sleep(5)
p.stdin.write("4\n".encode())
p.stdin.flush()

while True:
  input()
