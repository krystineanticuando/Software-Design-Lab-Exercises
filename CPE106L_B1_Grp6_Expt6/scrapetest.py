from urllib.request import urlopen
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
html = urlopen("http://pythonscraping.com/pages/page1.html")
# html = urlopen('https://www.mapua.edu.ph/')
print(html.read())