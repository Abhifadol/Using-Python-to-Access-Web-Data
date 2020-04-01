import urllib
from bs4 import BeautifulSoup
url = raw_input('Enter Url: ')
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position:"))
for i in range(count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)
    
    print(s[position-1])
    print(t[position-1])
    url = s[position-1]
