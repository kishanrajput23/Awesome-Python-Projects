import requests;
import webbrowser;
from bs4 import BeautifulSoup as bs;

githubUsername = input("Enter the GitHub Username : ");
url = 'https://github.com/' + githubUsername;

# requesting the data for the url
requestData = requests.get(url);

# parsing the data using the beautiful soup library
parsedData = bs(requestData.content, 'html.parser');

# getting the profile image link from the parsed data
profileImageUrl = parsedData.find('img',{'alt' : "Avatar"})['src'];

# displaying the profile image link
print("Link to the profile Image :" + profileImageUrl);

# code to open a image url in a new browser tab
webbrowser.open(profileImageUrl, new=2)