import requests
from bs4 import BeautifulSoup
 
 
url = 'https://www.python.org/'
# make a request
reqs = requests.get(url)
# download the html content
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
# find all anchor tags
for link in soup.find_all('a'):
    # extract the value inside href
    print(link.get('href'))