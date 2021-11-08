from urllib.request import urlopen
from bs4 import BeautifulSoup


# open url page and retrieve the content
html = urlopen('http://jr.jd.com')

#print(html.read())

#transfer html content to bs object
bs_obj = BeautifulSoup(html.read(), 'html.parser')

#look for all 'a' labels with class="nav-item-primary'
text_list = bs_obj.find_all("a", "nav-item-primary")

for text in text_list:
    print(text.get_text())

html.close()
