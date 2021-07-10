import os, sys
import json
import dotenv
dotenv.load_dotenv()

import getter  # type: ignore

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


# import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)


@app.route('/')
def hello_world_handler():
    return 'Hello from the Raspberry Pi moniter api!'

@app.route('/get_data')
def get_data_handler():
    print("Get Data")
    data = getter.get_data()

    return json.dumps(data)

@app.route('/get_loss')
def get_loss_handler():
    data = getter.get_loss()

    return json.dumps(data)


if __name__ == "__main__":
    port = os.getenv("PORT") if os.getenv("PORT") else 4040
    print("Running on port: ", port)
    app.run(host="0.0.0.0", port= port )