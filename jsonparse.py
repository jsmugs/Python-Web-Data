from urllib.request import urlopen
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen('http://py4e-data.dr-chuck.net/comments_1397806.json', context=ctx).read()
data = html.decode()
js = json.loads(data)

lst = []
for x in js['comments']:
    nw = x.get('count')
    lst.append(int(nw))

print('Count: ', len(lst))
print('Sum: ', sum(lst))