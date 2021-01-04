import requests
from bs4 import BeautifulSoup
import re

#url = 'https://en.wikipedia.org/wiki/American_Airlines_Flight_587'

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script'
]
forbidden = [
    'shit',
    'fuck',
    'terrorist',
    'bomb',
    'explosion',
    'crashed',
    'killed',
    'accident',
    'slammed',
    'aircraft'
]

while True:
    url = input("url: ")
    try:
        res = requests.get(url)
        html_page = res.content
        soup = BeautifulSoup(html_page, 'html.parser')
        text = soup.find_all(text=True)
        
        for t in text:
            if t.parent.name not in blacklist:
                output += '{} '.format(t).lower()
                
        x = re.findall(r'\bterrorist\b|\bbomb\b|\baircraft\b', output)
        print(x)
        break
    except requests.exceptions.MissingSchema:
        print('invalid url, try again')
        continue




