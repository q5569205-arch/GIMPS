import subprocess
from keep_alive import keep_alive

keep_alive()

subprocess.run(["./mprime", "-m"])
