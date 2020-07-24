import requests, io, csv
from lxml import html

CFTC_URL = r"https://en.wikipedia.org/wiki/2013_New_England_Revolution_season"
data = io.StringIO(requests.get(CFTC_URL).text)

dialect = csv.Sniffer().sniff(data.read(1024))
data.seek(0)
reader = csv.reader(data, dialect)
for row in reader:
    print(row)

    
