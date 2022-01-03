import urllib.request, urllib.parse
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42
jsn = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter address: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    parms['key'] = api_key

    url = jsn + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx).read()
    data = connection.decode()
    js = json.loads(data)

    print(json.dumps(js, indent = 4))
    print(js['results'][0]['place_id'])
