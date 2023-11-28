# Introduction
We know weather updates are how much important in our day-to-day life. So, I am introducing the logic and script with some easiest way to understand for everyone. Let’s see a simple Python script to show the live update for Weather information. 

# Modules Needed
In this script, we are using some libraries

- bs4: Beautiful Soup(bs4) is a Python library for pulling data out of HTML and XML files. To install this module type the below command in the terminal. 

  pip install bs4

- win10toast: This library helps in creating desktop notifications. To install this module type the below command in the terminal.

  pip install win10toast

- requests: This library allows you to send HTTP/1.1 requests extremely easily.To install this module type the below command in the terminal.  

  pip install requests

# Approach :

- Extract data form given URL.
- Scrape the data with the help of requests and Beautiful Soup.
- Convert that data into html code.
- Find the required details and filter them.
- Save the result in the String.
- Pass the result in Notification object.

# Let’s execute the script step-by-step :

Step 1: Import all dependence
code:
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

Step 2: Create an object of ToastNotifier class.
code:
n = ToastNotifier()

Step 3: Define a function for getting data from the given url.
code:
def getdata(url):
    r = requests.get(url)  
    return r.text

Step 4: Now pass the URL into the getdata function and Convert that data into HTML code.
code:
htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup.prettify())

Step 5: Find the required details and filter them.
code:
current_temp = soup.find_all("span",
							class_=" _-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
chances_rain = soup.find_all("div",
							class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")
temp = (str(current_temp))
temp_rain = str(chances_rain)
result = "current_temp " + temp[128:-9] + " in patna bihar" + "\n" +temp_rain[131:-14]

Step 6: Now pass the result into notifications object.
code:
n.show_toast("Weather update", result, duration = 10)

# With this ,we have successfully made our first simple live weather desktop notifier.



