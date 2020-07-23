import requests, io, csv

CFTC_URL = r"https://ericversaw.netlify.app/aboutme"
data = io.StringIO(requests.get(CFTC_URL).text)

dialect = csv.Sniffer().sniff(data.read(1024))
data.seek(0)
reader = csv.reader(data, dialect)
for row in reader:
    print(row)

    
