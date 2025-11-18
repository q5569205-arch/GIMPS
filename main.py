import subprocess
import time

from keep_alive import keep_alive

keep_alive()

p = subprocess.Popen(["./GIMPS/mprime", "-m"], stdin=subprocess.PIPE)
time.sleep(5)
p.stdin.write("4\n".encode())
p.stdin.flush()

while True:
  input()
