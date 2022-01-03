from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Hadia.html'
pos = 18
tmz = 7

for i in range(tmz):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    span = soup('a')
    count = 0
    for tags in span:
        count += 1

        if count > pos:
            break

        url = tags.get('href', None)
print(url)

