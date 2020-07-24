##import requests
##from bs4 import BeautifulSoup
##
##url = "https://en.wikipedia.org/wiki/2013_New_England_Revolution_season"
##html = requests.get(url)
##soup = BeautifulSoup(html)
##
### kill all script and style elements
##for script in soup(["script", "style"]):
##    script.extract()    # rip it out
##
### get text
##text = soup.get_text()
##
### break into lines and remove leading and trailing space on each
##lines = (line.strip() for line in text.splitlines())
### break multi-headlines into a line each
##chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
### drop blank lines
##text = '\n'.join(chunk for chunk in chunks if chunk)
##
##stringText = text.text
##print(text)


import urllib
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/2013_New_England_Revolution_season"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()# rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

for texts in text:
    texts = str(texts.text)

print(text)


##import requests
##import re
##
##fp = urllib.request.urlopen("https://en.wikipedia.org/wiki/2013_New_England_Revolution_season")
##url = "https://en.wikipedia.org/wiki/2013_New_England_Revolution_season"
##url2 = requests.get(url)
##htmltext = url2.text
##
##
##print(htmltext)
