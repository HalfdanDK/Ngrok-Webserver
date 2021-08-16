import os
import threading

from flask import Flask
from pyngrok import ngrok

os.environ["FLASK_ENV"] = "development"

app = Flask(__name__)


public_url = ngrok.connect(5000).public_url
print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}/\"".format(public_url, 5000))

app.config["BASE_URL"] = public_url


@app.route("/")
def index():
    return "Hello from Localhost!"

threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()