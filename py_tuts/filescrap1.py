import requests
from bs4 import BeautifulSoup
url = "http://coredogs.com/lesson/web-page-tables.html"
req = requests.get(url)
htmlcontent = req.content
soup = BeautifulSoup(htmlcontent,'html.parser')
print(htmlcontent)
