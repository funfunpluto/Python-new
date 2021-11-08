from urllib.request import urlopen
from bs4 import BeautifulSoup


# open url page and retrieve the content
html = urlopen('http://jr.jd.com')

print(html.read())


html.close()
