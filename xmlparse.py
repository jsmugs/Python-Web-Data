from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen('http://py4e-data.dr-chuck.net/comments_1397805.xml', context=ctx).read()
tree = ET.fromstring(html)

cool = tree.findall('comments/comment')
lst = []
for item in cool:
    x = item.find('count').text
    lst.append(int(x))
print('Count: ',len(lst))
print('Sum: ', sum(lst))
