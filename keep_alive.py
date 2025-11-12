from threading import Thread
import subprocess

try:
  from flask import Flask, render_template
except:
  subprocess.run(["pip","install","flask"])
  from flask import Flask, render_template
  
app = Flask(__name__)


@app.route('/')
def index():
  return "Alive"


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()
