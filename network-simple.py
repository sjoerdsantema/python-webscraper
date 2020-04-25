from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# ignore ssl errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ask for number of sequences and position
position = int(input('Position:'))
totcount = int(input('Count:'))
url = input('URL:')
count = 0

# follow the url, at the defined position, x number of times
while count < totcount:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    for tag in tags[position-1:position]:
        print(count)
        print(tag.get('href', None), tag.contents[0])
        url = tag.get('href', None)
    count = count + 1
        



    


   

