## Url Web scraper

Scraping is a very essential skill for everyone to get data from any website.

### Module Needed:

- bs4: Beautiful Soup(bs4) is a Python library for pulling data out of HTML and XML files. This module does not come built-in with Python. To install this type the below command in the terminal.
- requests: Requests allows you to send HTTP/1.1 requests extremely easily. This module also does not comes built-in with Python. To install this type the below command in the terminal.

### Code:

```{python}
import requests
from bs4 import BeautifulSoup


url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all('a'):
    print(link.get('href'))
```

### Working:

Here we are importing the beautifulsoup from bs4 to convert the document to it’s Unicode, and then further HTML entities are converted to Unicode characters. Then we just iterate through the list of all those links and print one by one. The reqs here is of response type i.e. we are fetching it as a response for the http request of our URL. We are then passing that string as one the parameter to the beautifulsoup and then finally iterating all the links found.

### Screenshot:

![url web scraper output](https://user-images.githubusercontent.com/67074796/193414565-db713a45-ba31-44af-ad47-60383bba7b42.png)
